from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select
from app.core.database import get_session
from app.models.roles import Role, Permission 

router = APIRouter()
@router.get("/", response_model=List[Role])
async def read_roles(db: AsyncSession = Depends(get_session)):
    result = await db.execute(select(Role))
    return result.scalars().all()
@router.post("/", response_model=Role)
async def create_role(role: Role, db: AsyncSession = Depends(get_session)):
    db.add(role)
    await db.commit()
    await db.refresh(role)
    return role
@router.put("/{role_id}", response_model=Role)
async def update_role(role_id: str, role_in: Role, db: AsyncSession = Depends(get_session)):
    role = await db.get(Role, role_id)
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")
    role.role_name = role_in.role_name
    role.role_description = role_in.role_description
    db.add(role)
    await db.commit()
    await db.refresh(role)
    return role

@router.get("/permissions", response_model=List[Permission])
async def read_all_permissions(db: AsyncSession = Depends(get_session)):
    result = await db.execute(select(Permission))
    return result.scalars().all()
@router.put("/{role_id}/permissions")
async def update_role_permissions(
    role_id: str, 
    permissions: List[Permission], 
    db: AsyncSession = Depends(get_session)
):
    
    existing = await db.execute(select(Permission).where(Permission.role_id == role_id))
    for p in existing.scalars().all():
        await db.delete(p)
    
    for p in permissions:
        
        new_perm = Permission(
            role_id=role_id,
            module_name=p.module_name,
            can_view=p.can_view,
            can_edit=p.can_edit,
            can_create=p.can_create,
            can_delete=p.can_delete,
            can_bulk_actions=p.can_bulk_actions
        )
        db.add(new_perm)
    await db.commit()
    return {"status": "success"}