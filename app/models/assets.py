from rest_framework.fields import Field
from app.models.base import UUIDModel
from sqlmodel import Field
from typing import Optional

class DigitalAsset(UUIDModel,table=True):
    __tablename__='digital_assets'
    file_name:str
    file_url:str
    file_type:str
    file_size:str
    public_id:str 
    user_id:Optional[str]=None