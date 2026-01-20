from typing import Optional,Dict
from sqlmodel import SQLModel,Field,Column,JSON
from .base import UUIDModel
from app.models.base import UUIDModel
class Brand(UUIDModel,table=True):
    __tablename__='brand_master'
    brand_code:str=Field(unique=True,index=True)
    brand_name:str
    brand_logo:Optional[str]=None
    mfg_code:Optional[str]=None
    mfg_name:Optional[str]=None
    
class Vendor(UUIDModel,table=True):
    __tablename__='vendor_master'
    vendor_code:str=Field(unique=True,index=True)
    vendor_name:str
    contact_email:Optional[str]=None
    contact_phone:Optional[str]=None
    business_type:Optional[str]=None
    industry:Optional[str]=None

class Category(UUIDModel,table=True):
    __tablename__='category_master'
    category_code:str=Field(unique=True,index=True)
    industry_name:Optional[str]=None
    category_1:str
    category_2:Optional[str]=None
    breadcrum:Optional[str]=None
    
class Industry(UUIDModel,table=True):
    __tablename__='industry_master'
    industry_code:str=Field(unique=True,index=True)
    industry_name:str
    is_active:bool=True
    
class  Attribute(UUIDModel,table=True):
    __tablename__='attribute_master'
    attribute_code:str=Field(unique=True,index=True)
    attribute_name:str
    industry_name:Optional[str]=None
    description:Optional[str]=None
    applicable_categories:Optional[str]=None
    attribute_type:Optional[str]=None
    data_type:Optional[str]=None
    unit:Optional[str]=None
    filter:Optional[str]='No'
    filter_display_name:Optional[str]=None
    usage_count:int=0
    values_data: Dict = Field(default={}, sa_column=Column(JSON)) 
    attribute_value_1: Optional[str] = ""
    attribute_uom_1: Optional[str] = ""