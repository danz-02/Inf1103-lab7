from physical import physical_Product
from digital import Digital_Product
from Inheritance_product import Product


class Inventory: 
    
    def __init__(self): 
        self.__product=[]

    def get_products(self):
       return self.__product

    def add_product(self, product):
        product = self.__product.append(product)

    def search_product(self, id):
        for product in self.__product:
            ##'OOP' search product by 'id'
            if product.get_id() == id:
                return product 

    def display(self):
        print("\nCurrent Inventory\n" "--------------------------------------------")
        for product in self.__product:
        
            if isinstance(product, physical_Product):

                print(f"ID: {product.get_id()}, Name: {product.get_name()}, Price: {product.get_price()}, Stock Quantity: {product.get_stock()}, Physical Product: {product.get_physical_weight()}")

            if isinstance(product, Digital_Product):
                print(f"ID: {product.get_id()}, Name: {product.get_name()}, Price: {product.get_price()}, Stock Quantity: {product.get_stock()}, Digital Product: {product.get_download_size()}")
        print("--------------------------------------------\n") ##Display 