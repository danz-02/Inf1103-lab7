from Inheritance_product import Product
from canBeShipped import CanBeShipped



class physical_Product(Product, CanBeShipped): 
        def __init__(self, get_id, get_name, get_stock, update_stock, physical_weight): 
            super().__init__(get_id, get_name, get_stock, update_stock) ##calling parent
            self._physical_weight = physical_weight

        def get_physical_weight(self):
            return (self._physical_weight)

        def  get_fulfilment_info(self):
            print("This product requires physical shipping.")


        def display_product(self): 
            super().display_product()  ##Extract from infomation from 'parent' 
            print(f"This products has a weight of {self._physical_weight} Kg!")

        def calculate_shipping_cost(self):
            cost = self._physical_weight *2 ##Initialise own calculation
            return
