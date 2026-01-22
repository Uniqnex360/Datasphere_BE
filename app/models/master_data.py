from typing import Optional, Dict
from sqlmodel import Field, Column, JSON
from .base import UUIDModel

class Brand(UUIDModel, table=True):
    __tablename__ = "brand_master"
    brand_code: str = Field(unique=True, index=True)
    brand_name: str
    brand_logo: Optional[str] = None
    mfg_code: Optional[str] = None
    mfg_name: Optional[str] = None

class Vendor(UUIDModel, table=True):
    __tablename__ = "vendor_master"
    vendor_code: str = Field(unique=True, index=True)
    vendor_name: str
    contact_email: Optional[str] = None
    contact_phone: Optional[str] = None
    business_type: Optional[str] = None
    industry: Optional[str] = None

class Category(UUIDModel, table=True):
    __tablename__ = "category_master"
    category_code: str = Field(unique=True, index=True)
    industry_name: Optional[str] = None
    category_1: str
    category_2: Optional[str] = None
    category_3: Optional[str] = None
    category_4: Optional[str] = None
    category_5: Optional[str] = None
    category_6: Optional[str] = None
    category_7: Optional[str] = None
    category_8: Optional[str] = None
    breadcrumb: Optional[str] = None
    product_type: Optional[str] = None

class Industry(UUIDModel, table=True):
    __tablename__ = "industry_master"
    industry_code: str = Field(unique=True, index=True)
    industry_name: str
    is_active: bool = True

class Attribute(UUIDModel, table=True):
    __tablename__ = "attribute_master"
    
    attribute_code: str = Field(unique=True, index=True)
    attribute_name: str
    industry_name: Optional[str] = None
    industry_attribute_name: Optional[str] = None
    description: Optional[str] = None
    applicable_categories: Optional[str] = None
    attribute_type: Optional[str] = None
    data_type: Optional[str] = None
    unit: Optional[str] = None
    filter: Optional[str] = "No"
    filter_display_name: Optional[str] = None
    usage_count: int = 0
    values_data: Dict = Field(default={}, sa_column=Column(JSON))

    # Explicit 1-50
    attribute_value_1: Optional[str] = None
    attribute_uom_1: Optional[str] = None
    attribute_value_2: Optional[str] = None
    attribute_uom_2: Optional[str] = None
    attribute_value_3: Optional[str] = None
    attribute_uom_3: Optional[str] = None
    attribute_value_4: Optional[str] = None
    attribute_uom_4: Optional[str] = None
    attribute_value_5: Optional[str] = None
    attribute_uom_5: Optional[str] = None
    attribute_value_6: Optional[str] = None
    attribute_uom_6: Optional[str] = None
    attribute_value_7: Optional[str] = None
    attribute_uom_7: Optional[str] = None
    attribute_value_8: Optional[str] = None
    attribute_uom_8: Optional[str] = None
    attribute_value_9: Optional[str] = None
    attribute_uom_9: Optional[str] = None
    attribute_value_10: Optional[str] = None
    attribute_uom_10: Optional[str] = None
    attribute_value_11: Optional[str] = None
    attribute_uom_11: Optional[str] = None
    attribute_value_12: Optional[str] = None
    attribute_uom_12: Optional[str] = None
    attribute_value_13: Optional[str] = None
    attribute_uom_13: Optional[str] = None
    attribute_value_14: Optional[str] = None
    attribute_uom_14: Optional[str] = None
    attribute_value_15: Optional[str] = None
    attribute_uom_15: Optional[str] = None
    attribute_value_16: Optional[str] = None
    attribute_uom_16: Optional[str] = None
    attribute_value_17: Optional[str] = None
    attribute_uom_17: Optional[str] = None
    attribute_value_18: Optional[str] = None
    attribute_uom_18: Optional[str] = None
    attribute_value_19: Optional[str] = None
    attribute_uom_19: Optional[str] = None
    attribute_value_20: Optional[str] = None
    attribute_uom_20: Optional[str] = None
    attribute_value_21: Optional[str] = None
    attribute_uom_21: Optional[str] = None
    attribute_value_22: Optional[str] = None
    attribute_uom_22: Optional[str] = None
    attribute_value_23: Optional[str] = None
    attribute_uom_23: Optional[str] = None
    attribute_value_24: Optional[str] = None
    attribute_uom_24: Optional[str] = None
    attribute_value_25: Optional[str] = None
    attribute_uom_25: Optional[str] = None
    attribute_value_26: Optional[str] = None
    attribute_uom_26: Optional[str] = None
    attribute_value_27: Optional[str] = None
    attribute_uom_27: Optional[str] = None
    attribute_value_28: Optional[str] = None
    attribute_uom_28: Optional[str] = None
    attribute_value_29: Optional[str] = None
    attribute_uom_29: Optional[str] = None
    attribute_value_30: Optional[str] = None
    attribute_uom_30: Optional[str] = None
    attribute_value_31: Optional[str] = None
    attribute_uom_31: Optional[str] = None
    attribute_value_32: Optional[str] = None
    attribute_uom_32: Optional[str] = None
    attribute_value_33: Optional[str] = None
    attribute_uom_33: Optional[str] = None
    attribute_value_34: Optional[str] = None
    attribute_uom_34: Optional[str] = None
    attribute_value_35: Optional[str] = None
    attribute_uom_35: Optional[str] = None
    attribute_value_36: Optional[str] = None
    attribute_uom_36: Optional[str] = None
    attribute_value_37: Optional[str] = None
    attribute_uom_37: Optional[str] = None
    attribute_value_38: Optional[str] = None
    attribute_uom_38: Optional[str] = None
    attribute_value_39: Optional[str] = None
    attribute_uom_39: Optional[str] = None
    attribute_value_40: Optional[str] = None
    attribute_uom_40: Optional[str] = None
    attribute_value_41: Optional[str] = None
    attribute_uom_41: Optional[str] = None
    attribute_value_42: Optional[str] = None
    attribute_uom_42: Optional[str] = None
    attribute_value_43: Optional[str] = None
    attribute_uom_43: Optional[str] = None
    attribute_value_44: Optional[str] = None
    attribute_uom_44: Optional[str] = None
    attribute_value_45: Optional[str] = None
    attribute_uom_45: Optional[str] = None
    attribute_value_46: Optional[str] = None
    attribute_uom_46: Optional[str] = None
    attribute_value_47: Optional[str] = None
    attribute_uom_47: Optional[str] = None
    attribute_value_48: Optional[str] = None
    attribute_uom_48: Optional[str] = None
    attribute_value_49: Optional[str] = None
    attribute_uom_49: Optional[str] = None
    attribute_value_50: Optional[str] = None
    attribute_uom_50: Optional[str] = None