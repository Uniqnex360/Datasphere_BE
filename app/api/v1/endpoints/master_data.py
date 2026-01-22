from sqlalchemy.exc import IntegrityError 
from typing import List, Type
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select, SQLModel
from app.core.database import get_session
from fastapi import HTTPException

from app.models.master_data import Attribute, Brand, Category, Industry, Vendor
router=APIRouter()
def create_crud_routes(model:Type[SQLModel],prefix:str):
    @router.get(f"/{prefix}",response_model=List[model])
    async def read_items(db:AsyncSession=Depends(get_session)):
        result=await db.execute(select(model))
        return result.scalars().all()
    @router.post(f'/{prefix}',response_model=model)
    async def create_item(item:model,db:AsyncSession=Depends(get_session)):
        try:
            db.add(item)
            await db.commit()
            await db.refresh(item)
            return item
        except IntegrityError as e:
            await db.rollback()
            error_detail=str(e.orig)
            
            if 'duplicate key' in  error_detail:
                import re
                match = re.search(r'constraint "([^"]+)"', error_detail)
                constraint_name=match.group(1) if match else 'unique_constraint'
                value_match = re.search(r'Key \(([^)]+)\)=\(([^)]+)\)', error_detail)
                if value_match:
                    field_name = value_match.group(1)
                    field_value = value_match.group(2)
                    raise HTTPException(
                    status_code=400,
                    detail=f'{field_name} "{field_value}" already exists!'
                )
                raise HTTPException(
                status_code=400,
                detail=f'Duplicate entry violates {constraint_name}. Record already exists!'
            )
            raise HTTPException(status_code=400, detail=str(e.orig))
        except Exception as e:
            await db.rollback()
            raise HTTPException(status_code=500,detail=str(e))
    
    
create_crud_routes(Brand,'brands')
create_crud_routes(Category,'categories')
create_crud_routes(Vendor,'vendors')
create_crud_routes(Industry,'industries')
create_crud_routes(Attribute,'attributes')