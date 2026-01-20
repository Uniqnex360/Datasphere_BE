from typing import List, Type
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select, SQLModel
from app.core.database import get_session

from app.models.master_data import Attribute, Brand, Category, Industry, Vendor
router=APIRouter()
def create_crud_routes(model:Type[SQLModel],prefix:str):
    @router.get(f"/{prefix}",response_model=List[model])
    async def read_items(db:AsyncSession=Depends(get_session)):
        result=await db.execute(select(model))
        return result.scalars().all()
    @router.post(f'/{prefix}',response_model=model)
    async def create_item(item:model,db:AsyncSession=Depends(get_session)):
        db.add(item)
        await db.commit()
        await db.refresh(item)
        return item
    
create_crud_routes(Brand,'brands')
create_crud_routes(Category,'categories')
create_crud_routes(Vendor,'vendors')
create_crud_routes(Industry,'industries')
create_crud_routes(Attribute,'attributes')