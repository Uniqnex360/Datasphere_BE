from typing import Optional, List, Dict
from sqlmodel import Field, Column, JSON
from .base import UUIDModel
class Channel(UUIDModel, table=True):
    __tablename__ = "channels"
    channel_name: str = Field(index=True)
    channel_status: str = Field(default="active")
    template_headers: List[str] = Field(default=[], sa_column=Column(JSON))
    last_export_date: Optional[str] = None
    products_mapped_count: int = 0
class ChannelFieldMapping(UUIDModel, table=True):
    __tablename__ = "channel_field_mappings"
    channel_id: str = Field(index=True)
    pim_field: str
    channel_field: str
    mapping_type: str 
    static_value: Optional[str] = None
    concatenation_pattern: Optional[str] = None
    is_required: bool = False
class ChannelExport(UUIDModel, table=True):
    __tablename__ = "channel_exports"
    channel_id: str
    export_date: str
    product_count: int
    file_url: Optional[str] = None
    filters_applied: Dict = Field(default={}, sa_column=Column(JSON))
    status: str = "processing"