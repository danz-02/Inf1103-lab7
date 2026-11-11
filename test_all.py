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

print("Test Aggregation Part 3")
inventoryA = Inventory()
inventoryB = Inventory()

print("\nAdding product to Inventory A:")
inventoryA.add_product(phy)
inventoryA.display()

print("\nRemoving product from Inventory A:")
inventoryA.remove_product("P001")
inventoryA.display()

print("\nAdding same product to Inventory B:")
inventoryB.add_product(phy)
inventoryB.display()    
#----------------------------------------#

print("Test composition Part 4")

order1 = Order("0001")
order1.add_order_line(phy, 3)
order1.add_order_line(digital, 1)
order1.display_order()

#----------------------------------------#

print("Liskov Substitution Principle (LSP) Part 6")
print()
def show_product_details(product: Product) -> None:
    product.display_product()
    product.get_fulfilment_info()

show_product_details(phy)
print()

#----------------------------------------#