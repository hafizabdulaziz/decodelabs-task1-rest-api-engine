from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas.product import Product, ProductCreate
from app.db.store import store

router = APIRouter()

@router.post("/", response_model=Product)
def create_product(product_in: ProductCreate):
    return store.create(product_in.model_dump())

@router.get("/", response_model=List[Product])
def get_products():
    return store.get_all()

@router.get("/{product_id}", response_model=Product)
def get_product(product_id: int):
    product = store.get_by_id(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product
