from abc import ABC, abstractmethod
from supplier import Supplier


class Product(ABC):

    def __init__(self, id: str, name: str, price: float, stock_quantity: int, supplier: Supplier):

        self._id:str = id
        self._name: str = name
        self._price: str = price
        self._stock_quantity: str = stock_quantity
        self.supplier: Supplier = supplier

    def get_id(self):
        return (self._id)


    def get_name(self):
        return (self._name)

    def get_price(self):
        return (self._price)

    def get_stock(self):
        return (self._stock_quantity)

    def update_stock(self, stock_update):
        self._stock_quantity = stock_update


    def display_product(self):

        print(f"ID: {self._id} | Name: {self._name} | Price: ${self._price:.2f} | Stock: {self._stock_quantity}", end="")

    @abstractmethod
    def get_fulfilment_info():

        pass
