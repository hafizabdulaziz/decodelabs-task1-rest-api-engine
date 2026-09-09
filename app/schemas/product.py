from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, List

class ProductBase(BaseModel):
    title: str = Field(..., json_schema_extra={"example": "Smartphone"})
    description: Optional[str] = Field(None, json_schema_extra={"example": "A powerful smartphone"})
    price: float = Field(..., gt=0, json_schema_extra={"example": 999.99})

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: int = Field(..., json_schema_extra={"example": 1})

    model_config = ConfigDict(from_attributes=True)

class ProductPaginated(BaseModel):
    total: int
    page: int
    size: int
    items: List[Product]
