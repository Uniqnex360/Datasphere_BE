from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime
import uuid

class DigitalAsset(SQLModel, table=True):
    __tablename__ = "digital_assets"
    
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    file_name: str
    file_url: str
    file_type: str  
    file_size: int
    public_id: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow) 