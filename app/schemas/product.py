from pydantic import BaseModel, Field
from typing import Optional

class ProductBase(BaseModel):
    name: str = Field(..., example="Smartphone")
    description: Optional[str] = Field(None, example="A powerful smartphone")
    price: float = Field(..., gt=0, example=999.99)

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: int = Field(..., example=1)

    class Config:
        from_attributes = True
