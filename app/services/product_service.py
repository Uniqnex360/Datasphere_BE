from app.models.product import Product
from app.schemas.product import ProductCreate,ProductUpdate
from sqlalchemy.ext.asyncio import AsyncSession
from app.services.base import CRUDBase
from sqlmodel import select
from typing import Optional
class CRUDProduct(CRUDBase[Product,ProductCreate,ProductUpdate]):
    async def get_by_code(self,db:AsyncSession,code:str)->Optional[Product]:
        query=select(Product).where(Product.product_code==code)
        result = await db.execute(query)
        return result.scalars().one_or_none()
    async def upsert(self,db:AsyncSession,product_in:ProductCreate)->Product:
        if product_in.product_code:
            product_in.product_code=product_in.product_code.strip()
        existing=await self.get_by_code(db,product_in.product_code)
        if existing:
            print(f"🔄 Upsert: Updating existing product {product_in.product_code}")
            update_data=product_in.model_dump(exclude_unset=True)
            for key,value in update_data.items():
                setattr(existing,key,value)
            db.add(existing)
            await db.commit()
            await db.refresh(existing)
            return existing
        else:
            print(f"🆕 Upsert: Creating new product {product_in.product_code}")
            db_obj = Product.model_validate(product_in)
            if not getattr(db_obj, "enrichment_status", None):
                db_obj.enrichment_status = "pending"
            if getattr(db_obj, "completeness_score", None) is None:
                db_obj.completeness_score = 0
            
            db.add(db_obj)
            await db.commit() 
            await db.refresh(db_obj)
            if not db_obj:
                raise ValueError("Database failed to return created object")
            return db_obj
                
product_service=CRUDProduct(Product)