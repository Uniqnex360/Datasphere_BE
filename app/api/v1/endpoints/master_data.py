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
        
    @router.put(f'/{prefix}/{{item_id}}', response_model=model)
    async def update_item(item_id: str, item_data: dict, db: AsyncSession = Depends(get_session)):
        try:
            pk_field = f'{prefix[:-1]}_code'
            
            result = await db.execute(select(model).where(getattr(model, pk_field) == item_id))
            existing_item = result.scalar_one_or_none()
            
            if not existing_item:
                raise HTTPException(
                    status_code=404, 
                    detail=f"{prefix[:-1].title()} with code '{item_id}' not found"
                )
            
            readonly_fields = {
                'id', 'created_at', 'updated_at', 
                f'{prefix[:-1]}_code'  
            }
            
            for field, value in item_data.items():
                if field not in readonly_fields and hasattr(existing_item, field) and value is not None:
                    setattr(existing_item, field, value)
            
            if hasattr(existing_item, 'updated_at'):
                from datetime import datetime
                existing_item.updated_at = datetime.utcnow()
            
            await db.commit()
            await db.refresh(existing_item)
            return existing_item
            
        except HTTPException:
            raise
        except Exception as e:
            await db.rollback()
            raise HTTPException(status_code=500, detail=f"Failed to update {prefix[:-1]}: {str(e)}")
    
    @router.delete(f'/{prefix}/{{item_id}}')
    async def delete_item(item_id: str, db: AsyncSession = Depends(get_session)):
        try:
            pk_field = f'{prefix[:-1]}_code'  
            
            # Get existing item
            result = await db.execute(select(model).where(getattr(model, pk_field) == item_id))
            existing_item = result.scalar_one_or_none()
            
            if not existing_item:
                raise HTTPException(
                    status_code=404, 
                    detail=f"{prefix[:-1].title()} with code '{item_id}' not found"
                )
            
            
            await db.delete(existing_item)
            await db.commit()
            
            return {
                "message": f"{prefix[:-1].title()} '{item_id}' deleted successfully",
                "deleted_id": item_id
            }
            
        except HTTPException:
            raise
        except IntegrityError as e:
            await db.rollback()
            error_detail = str(e.orig)
            
            if 'foreign key constraint' in error_detail.lower():
                raise HTTPException(
                    status_code=409,
                    detail=f"Cannot delete {prefix[:-1]}. It is referenced by other records."
                )
            raise HTTPException(status_code=409, detail="Cannot delete due to data constraints")
        except Exception as e:
            await db.rollback()
            raise HTTPException(status_code=500, detail=f"Failed to delete {prefix[:-1]}: {str(e)}")
    
create_crud_routes(Brand,'brands')
create_crud_routes(Category,'categories')
create_crud_routes(Vendor,'vendors')
create_crud_routes(Industry,'industries')
create_crud_routes(Attribute,'attributes')