from typing import List, Any
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select
from app.core.database import get_session
from app.models.channels import Channel, ChannelFieldMapping, ChannelExport
router = APIRouter()
@router.get("/", response_model=List[Channel])
async def read_channels(db: AsyncSession = Depends(get_session)):
    result = await db.execute(select(Channel))
    return result.scalars().all()
@router.post("/", response_model=Channel)
async def create_channel(channel: Channel, db: AsyncSession = Depends(get_session)):
    db.add(channel)
    await db.commit()
    await db.refresh(channel)
    return channel
@router.delete("/{channel_id}")
async def delete_channel(channel_id: str, db: AsyncSession = Depends(get_session)):
    channel = await db.get(Channel, channel_id)
    if not channel:
        raise HTTPException(status_code=404, detail="Channel not found")
    await db.delete(channel)
    await db.commit()
    return {"status": "success"}
@router.get("/{channel_id}/mappings", response_model=List[ChannelFieldMapping])
async def get_mappings(channel_id: str, db: AsyncSession = Depends(get_session)):
    query = select(ChannelFieldMapping).where(ChannelFieldMapping.channel_id == channel_id)
    result = await db.execute(query)
    return result.scalars().all()
@router.put("/{channel_id}/mappings")
async def update_mappings(
    channel_id: str, 
    mappings: List[ChannelFieldMapping], 
    db: AsyncSession = Depends(get_session)
):
    existing = await db.execute(select(ChannelFieldMapping).where(ChannelFieldMapping.channel_id == channel_id))
    for row in existing.scalars().all():
        await db.delete(row)
    for m in mappings:
        new_mapping = ChannelFieldMapping(
            channel_id=channel_id,
            pim_field=m.pim_field,
            channel_field=m.channel_field,
            mapping_type=m.mapping_type,
            static_value=m.static_value,
            concatenation_pattern=m.concatenation_pattern,
            is_required=m.is_required
        )
        db.add(new_mapping)
    await db.commit()
    return {"status": "success"}