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
        existing=await self.get_by_code(db,product_in.product_code)
        if existing:
            update_data=product_in.model_dump(exclude_unset=True)
            for key,value in update_data.items():
                setattr(existing,key,value)
            db.add(existing)
            await db.commit()
            await db.refresh(existing)
            return existing
        else:
            return await self.create(db, obj_in=product_in)
                
product_service=CRUDProduct(Product)