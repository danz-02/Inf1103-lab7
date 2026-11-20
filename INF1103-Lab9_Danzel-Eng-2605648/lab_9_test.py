from order import Order
from product_factory import BulkDiscount, PercentageDiscount, StudentDiscount, ProductFactory
from digital import Digital_Product
from physical import physical_Product
from supplier import Supplier
from helper import get_positive_float
from file_handling import load_products
from inventory import Inventory


def discount(supplier1):

    print("Test Discount")
    print("-------------------------")

    ##Product priced so the lines add up to 250 (5 x 50)
    course = Digital_Product("P003", "Course", 50.0, 10, supplier1, 100)
    order = Order("0003", BulkDiscount(200, 20))
    order.add_order_line(course, 5)

    print("Bulk discount:", order.calculate_total())      

    order.set_discount(PercentageDiscount(10))
    print("Percentage discount:", order.calculate_total())   
    print("-------------------------")
    print("")



def Percentage_Discount(supplier1):

    print("Testing code check for 2.4")
    shared = PercentageDiscount(10)
    order1 = Order("0005", shared)
    order2 = Order("0006", shared)

    print("Same strategy object?", order1.discount is order2.discount)   # True
    print(id(order1.discount), id(order2.discount))                      # same number twice

    # Fourth strategy, with Order untouched
    course = Digital_Product("P004", "Course 2", 50.0, 10, supplier1, 100)
    order1.add_order_line(course, 5)                                     # 250

    order1.set_discount(StudentDiscount())
    print("Student discount:", order1.calculate_total())                 # 212.5
    print("Order2 still uses its own:", type(order2.discount).__name__) # PercentageDiscount
    print("-------------------------")
    print("")


def test_shared_discount(pen):
    print("\nTest Association: shared discount (2.4)")
    print("-----------------")
    shared = PercentageDiscount(10)
    order_a = Order("OA", shared)
    order_b = Order("OB", shared)
    order_a.add_order_line(pen, 100)    # subtotal 250
    order_b.add_order_line(pen, 40)     # subtotal 100
 
    print("Same discount object:", order_a.discount is order_b.discount)
    print("Order A total:", order_a.calculate_total())
    print("Order B total:", order_b.calculate_total())



def check_postive_value():
    print("")
    print("Test positive values")
    price = get_positive_float("Enter the product price: ")
    print("You entered:", price)


def unknown_product_type(supplier):
    print("\nPredict: ProductFactory.create('service', ...)")
    print("-----------------")
    ProductFactory.create("service", "S1", "Install", 30, 5, supplier, 0)
    print("This line runs only if nothing raised an exception")


supplier1 = Supplier("S001", "Singapore Tech Ltd", "sg_tech@email.com")
pen = physical_Product("P005", "Pen", 2.5, 500, supplier1, 0.02)
my_inventory = Inventory()
discount(supplier1)
Percentage_Discount(supplier1)
test_shared_discount(pen)
check_postive_value()
load_products("lab_9_test.csv", my_inventory, supplier1)
#unknown_product_type(supplier1)


