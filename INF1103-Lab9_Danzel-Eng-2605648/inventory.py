from physical import physical_Product
from digital import Digital_Product
from Inheritance_product import Product


class Inventory: 
    
    def __init__(self): 
        self._product: list[Product] = []

    def get_products(self):
       return self._product

    def add_product(self, product: Product):
        product = self._product.append(product)

    def find_product(self, product_id: str) -> Product | None:
        for product in self._product:
            if product.get_id() == product_id:
                return product
        return None

    def remove_product(self, product_id: str):
        product = self.find_product(product_id)
        if product_id is not None:
            self._product.remove(product)

    def search_product(self, id: str):
        for product in self._product:
            ##'OOP' search product by 'id'
            if product.get_id() == id:
                return product 


    def display(self) -> None:
        for product in self._product:
            product.display_product()
        print("--------------------------------------------\n") ##Display 