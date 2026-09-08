from typing import List, Dict, Optional
from app.schemas.product import Product

class ProductStore:
    def __init__(self):
        self._products: Dict[int, Product] = {}
        self._next_id = 1

    def create(self, product_data: dict) -> Product:
        product = Product(id=self._next_id, **product_data)
        self._products[self._next_id] = product
        self._next_id += 1
        return product

    def get_all(self) -> List[Product]:
        return list(self._products.values())

    def get_by_id(self, product_id: int) -> Optional[Product]:
        return self._products.get(product_id)

store = ProductStore()
