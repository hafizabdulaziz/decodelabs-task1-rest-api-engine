from typing import Optional, List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func, or_, desc, asc
from app.db.models import Product as ProductModel
from app.schemas.product import Product as ProductSchema

class ProductStore:
    async def create(self, db: AsyncSession, product_data: ProductSchema) -> ProductModel:
        product = ProductModel(**product_data.model_dump())
        db.add(product)
        await db.commit()
        await db.refresh(product)
        return product

    async def get_all(self, db: AsyncSession, category: Optional[str] = None, search: Optional[str] = None, 
                      min_price: Optional[float] = None, max_price: Optional[float] = None, 
                      sort_by: Optional[str] = None, page: int = 1, size: int = 10) -> tuple[List[ProductModel], int]:
        query = select(ProductModel)

        if category:
            query = query.filter(ProductModel.category == category)
        if search:
            query = query.filter(or_(ProductModel.title.contains(search), ProductModel.description.contains(search)))
        if min_price is not None:
            query = query.filter(ProductModel.price >= min_price)
        if max_price is not None:
            query = query.filter(ProductModel.price <= max_price)

        # Count total
        count_query = select(func.count()).select_from(query.subquery())
        total = (await db.execute(count_query)).scalar()

        # Sorting
        if sort_by == "price_asc":
            query = query.order_by(asc(ProductModel.price))
        elif sort_by == "price_desc":
            query = query.order_by(desc(ProductModel.price))
        elif sort_by == "created_at":
            query = query.order_by(desc(ProductModel.created_at))

        # Pagination
        query = query.offset((page - 1) * size).limit(size)
        
        result = await db.execute(query)
        return result.scalars().all(), total

    async def get_by_id(self, db: AsyncSession, product_id: int) -> Optional[ProductModel]:
        result = await db.execute(select(ProductModel).filter(ProductModel.id == product_id))
        return result.scalars().first()

store = ProductStore()
