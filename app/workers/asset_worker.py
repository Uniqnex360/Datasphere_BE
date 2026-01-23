import logging
from sqlalchemy.exc import SQLAlchemyError

from app.core.database import async_session_factory
from app.services.product_service import product_service
from app.cloudinary_client import ingest_image_from_url
from app.models.assets import DigitalAsset

logger = logging.getLogger(__name__)


async def process_product_assets(product_code: str) -> None:
    logger.info("Starting asset ingestion for product_code=%s", product_code)

    async with async_session_factory() as db:
        try:
            product = await product_service.get_by_code(db, product_code)

            if not product:
                logger.warning("Product not found: %s", product_code)
                return

            updates_made = False

            for i in range(1, 6):
                field_name = f"image_url_{i}"

                if not hasattr(product, field_name):
                    continue

                current_url = getattr(product, field_name)

                if (
                    not current_url
                    or "http" not in current_url
                    or "cloudinary.com" in current_url
                ):
                    continue

                asset_public_id = f"{product.product_code}_img_{i}"

                try:
                    asset_data = ingest_image_from_url(current_url, asset_public_id)

                except Exception:
                    logger.exception(
                        "Image ingestion failed for product=%s image_index=%s",
                        product_code,
                        i,
                    )
                    continue

                if not asset_data:
                    logger.warning(
                        "No asset data returned for product=%s image_index=%s",
                        product_code,
                        i,
                    )
                    continue

                new_url = asset_data.get("secure_url")
                if not new_url:
                    logger.warning(
                        "Missing secure_url for product=%s image_index=%s",
                        product_code,
                        i,
                    )
                    continue

                setattr(product, field_name, new_url)
                updates_made = True

                try:
                    digital_asset = DigitalAsset(
                        file_name=f"{product.product_code}_Image_{i}.{asset_data.get('format')}",
                        file_url=new_url,
                        file_type="image",
                        file_size=asset_data.get("bytes", 0),
                        public_id=asset_data.get("public_id"),
                    )
                    db.add(digital_asset)
                except Exception:
                    logger.exception(
                        "Failed to create DigitalAsset record for product=%s image_index=%s",
                        product_code,
                        i,
                    )
                    continue

            if updates_made:
                db.add(product)
                await db.commit()
                logger.info("Asset ingestion completed for product_code=%s", product_code)
            else:
                logger.info(
                    "No updates required for product_code=%s", product_code
                )

        except SQLAlchemyError:
            await db.rollback()
            logger.exception(
                "Database error while processing assets for product_code=%s",
                product_code,
            )
            raise

        except Exception:
            await db.rollback()
            logger.exception(
                "Unexpected error while processing assets for product_code=%s",
                product_code,
            )
            raise
