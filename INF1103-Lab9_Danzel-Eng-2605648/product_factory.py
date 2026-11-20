
from physical import physical_Product
from digital import Digital_Product
from abc import ABC, abstractmethod
from Inheritance_product import Product
from supplier import Supplier


class ProductFactory:
    @staticmethod
    def create(product_type: str, product_id: str, name: str, price: float, stock_quantity: int, supplier: Supplier) -> Product:
        if product_type == "physical":
            return physical_Product(product_id, name, price, stock_quantity, supplier)
        elif product_type == "digital":
            return Digital_Product(product_id, name, price, stock_quantity, supplier)
        else:
            raise ValueError(f"Unknown product type: {product_type}")

class DiscountStrategy(ABC): 
        @abstractmethod 
        def apply(self, total: float) -> float: ##Base case
            pass

class NoDiscount(DiscountStrategy):
    def apply(self, total:float) -> float: ##Created new classes
        return total

class PercentageDiscount(DiscountStrategy):
    def __init__(self, percentage:float) -> None:
        self._percentage = percentage

    def apply(self, total: float) -> float:
        return total - (total * self._percentage / 100) 

class BulkDiscount(DiscountStrategy):
    def __init__(self, threshold: float, amount:float) -> None:
        self._threshold = threshold
        self._amount = amount

    def apply(self, total:float) ->float:
        if total >= self._threshold:
            return total - self._amount
        return total

class StudentDiscount(DiscountStrategy):
    def apply(self, total: float) -> float:
        return total * 0.85 