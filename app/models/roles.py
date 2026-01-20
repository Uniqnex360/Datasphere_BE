from typing import Optional
from sqlmodel import Field
from .base import UUIDModel

class Role(UUIDModel, table=True):
    __tablename__ = "roles"
    role_name: str
    role_description: Optional[str] = None
    is_super_admin: bool = False

class Permission(UUIDModel, table=True):
    __tablename__ = "permissions"
    role_id: str 
    module_name: str
    can_view: bool = False
    can_edit: bool = False
    can_create: bool = False
    can_delete: bool = False
    can_bulk_actions: bool = False