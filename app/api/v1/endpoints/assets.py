from typing import List
import uuid
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select
from app.core.database import get_session
from app.models.assets import DigitalAsset
router = APIRouter()
@router.get("/", response_model=List[DigitalAsset])
async def read_assets(db: AsyncSession = Depends(get_session)):
    try:
        result = await db.execute(select(DigitalAsset))
        return result.scalars().all()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
@router.post("/", response_model=DigitalAsset)
async def create_asset(asset: DigitalAsset, db: AsyncSession = Depends(get_session)):
    try:
        db.add(asset)
        await db.commit()
        await db.refresh(asset)
        return asset
    except Exception as e:
        await db.rollback() 
        raise HTTPException(status_code=400, detail="Could not create asset. Check inputs.")
@router.delete("/{asset_id}")
async def delete_asset(asset_id: str, db: AsyncSession = Depends(get_session)):
    try:
        asset_uuid = uuid.UUID(asset_id)
        asset = await db.get(DigitalAsset, asset_uuid)
        if not asset:
            raise HTTPException(status_code=404, detail="Asset not found")
        await db.delete(asset)
        await db.commit()
        return {"status": "success"}
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid ID format")
    except HTTPException as he:
        raise he
    except Exception as e:
        await db.rollback()
        raise HTTPException(status_code=500, detail=str(e))