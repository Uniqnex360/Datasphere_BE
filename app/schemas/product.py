from typing import Optional, Dict, Any
from pydantic import BaseModel, ConfigDict
from datetime import datetime
import uuid
class ProductBase(BaseModel):
    product_code: str
    product_name: str
    brand_name: Optional[str] = None
    brand_code: Optional[str] = None
    vendor_name: Optional[str] = None
    vendor_code: Optional[str] = None
    category_code: Optional[str] = None
    mpn: Optional[str] = None
    gtin: Optional[str] = None
    upc: Optional[str] = None
    ean: Optional[str] = None
    unspc: Optional[str] = None
    description: Optional[str] = None
    prod_short_desc: Optional[str] = None
    prod_long_desc: Optional[str] = None
    industry_name: Optional[str] = None
    category_1: Optional[str] = None
    category_2: Optional[str] = None
    category_3: Optional[str] = None
    features_1: Optional[str] = None
    features_2: Optional[str] = None
    features_3: Optional[str] = None
    features_4: Optional[str] = None
    features_5: Optional[str] = None
    features_6: Optional[str] = None
    features_7: Optional[str] = None
    features_8: Optional[str] = None
    features_9: Optional[str] = None
    features_10: Optional[str] = None
    image_url_1: Optional[str] = None
    image_url_2: Optional[str] = None
    image_url_3: Optional[str] = None
    image_url_4: Optional[str] = None
    image_url_5: Optional[str] = None
    attributes: Optional[Dict[str, Any]] = None
class ProductCreate(ProductBase):
    pass
class ProductUpdate(ProductBase):
    product_code: Optional[str] = None 
    product_name: Optional[str] = None
    enrichment_status: Optional[str] = None
    completeness_score: Optional[int] = None
class ProductResponse(ProductBase):
    id: uuid.UUID
    enrichment_status: str
    completeness_score: int
    created_at: datetime
    updated_at: datetime
    model_config = ConfigDict(from_attributes=True)