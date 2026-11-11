from supplier import Supplier
from physical import physical_Product
from digital import Digital_Product
from Inheritance_product import Product
from inventory import Inventory
from order import Order

inventory = Inventory()

supplier1 = Supplier("S001", "Singapore Tech Ltd", "sg_tech@email.com")

phy = physical_Product("P001", "Laptop", 999.0, 10, supplier1, 2.5)
digital = Digital_Product("P002", "E-book", 15.0, 100, supplier1, 100000)  # use your own digital args


print("Test Association (Supplier with Product) Part 2")
phy.supplier.display_supplier()
digital.supplier.display_supplier()

del supplier1
phy.supplier.display_supplier()
digital.supplier.display_supplier()

#------------------------------------#