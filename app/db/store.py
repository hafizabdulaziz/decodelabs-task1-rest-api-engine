from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.models import Product as ProductModel
from app.schemas.product import Product as ProductSchema

class ProductStore:
    async def create(self, db: AsyncSession, product_data: ProductSchema) -> ProductModel:
        product = ProductModel(**product_data.model_dump())
        db.add(product)
        await db.commit()
        await db.refresh(product)
        return product

    async def get_all(self, db: AsyncSession) -> list[ProductModel]:
        result = await db.execute(select(ProductModel))
        return result.scalars().all()

    async def get_by_id(self, db: AsyncSession, product_id: int) -> Optional[ProductModel]:
        result = await db.execute(select(ProductModel).filter(ProductModel.id == product_id))
        return result.scalars().first()

store = ProductStore()
