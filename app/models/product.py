from typing import Optional
from sqlmodel import Field, Column, JSON
from .base import UUIDModel

class Product(UUIDModel, table=True):
    __tablename__ = "product_master"

    product_code: str = Field(unique=True, index=True)
    product_name: str
    
    # Relationships
    parent_sku: Optional[str] = None
    brand_code: Optional[str] = None
    vendor_code: Optional[str] = None
    category_code: Optional[str] = None
    
    # Denormalized
    brand_name: Optional[str] = ""
    vendor_name: Optional[str] = ""
    mfg_name: Optional[str] = ""
    mfg_code: Optional[str] = ""
    industry_name: Optional[str] = ""
    industry_code: Optional[str] = ""
    
    # Categories
    category_1: Optional[str] = ""
    category_2: Optional[str] = ""
    category_3: Optional[str] = ""
    category_4: Optional[str] = ""
    category_5: Optional[str] = ""
    category_6: Optional[str] = ""
    category_7: Optional[str] = ""
    category_8: Optional[str] = ""
    
    # Product Info
    product_type: Optional[str] = ""
    variant_sku: Optional[str] = ""
    description: Optional[str] = ""
    model_series: Optional[str] = ""
    mpn: Optional[str] = Field(index=True, default="")
    gtin: Optional[str] = ""
    upc: Optional[str] = ""
    ean: Optional[str] = ""
    unspc: Optional[str] = ""
    
    # Descriptions
    prod_short_desc: Optional[str] = ""
    prod_long_desc: Optional[str] = ""
    
    # Features (1-10 based on migration)
    features_1: Optional[str] = ""
    features_2: Optional[str] = ""
    features_3: Optional[str] = ""
    features_4: Optional[str] = ""
    features_5: Optional[str] = ""
    features_6: Optional[str] = ""
    features_7: Optional[str] = ""
    features_8: Optional[str] = ""
    features_9: Optional[str] = ""
    features_10: Optional[str] = ""
    
    document_1_name: Optional[str] = ""
    document_1_url: Optional[str] = ""
    document_2_name: Optional[str] = ""
    document_2_url: Optional[str] = ""
    document_3_name: Optional[str] = ""
    document_3_url: Optional[str] = ""
    document_4_name: Optional[str] = ""
    document_4_url: Optional[str] = ""
    document_5_name: Optional[str] = ""
    document_5_url: Optional[str] = ""
    
    image_name_1: Optional[str] = ""
    image_url_1: Optional[str] = ""
    image_name_2: Optional[str] = ""
    image_url_2: Optional[str] = ""
    image_name_3: Optional[str] = ""
    image_url_3: Optional[str] = ""
    image_name_4: Optional[str] = ""
    image_url_4: Optional[str] = ""
    image_name_5: Optional[str] = ""
    image_url_5: Optional[str] = ""
    
    video_name_1: Optional[str] = ""
    video_url_1: Optional[str] = ""
    video_name_2: Optional[str] = ""
    video_url_2: Optional[str] = ""
    video_name_3: Optional[str] = ""
    video_url_3: Optional[str] = ""
    
    enrichment_status: str = Field(default="pending")
    completeness_score: int = Field(default=0)
    completeness_details: dict = Field(default={}, sa_column=Column(JSON))
    
    attributes: dict = Field(default={}, sa_column=Column(JSON))