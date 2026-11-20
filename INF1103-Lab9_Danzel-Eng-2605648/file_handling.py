import json
import os
import csv
from product_factory import ProductFactory 
from inventory import Inventory
from physical import physical_Product
from digital import Digital_Product
from supplier import Supplier


def load_inventory():
    ##Load previous transaction history
    orders = []
    inventory = Inventory()
    if os.path.exists("inventory.json"):
        try:
            with open("inventory.json", "r") as file:
                orders = json.load(file)
            if isinstance(orders, dict):      # NEW: a single product saved as { }
                orders = [orders]             # NEW: turn it into a list of one product
        except json.JSONDecodeError:
            orders = []
        print("inventory.json found.\n Inventory loaded successfully. ")

    else:
        ##No previous records, will automatically create a new file 
        orders=[]
        f=open("inventory.json", "w")
        f.close()

    for item in orders:

        if item['product_type'] == "physical":

            product = physical_Product(item["id"], item["name"], item["price"], item["stock_quantity"], item["weight"])
            inventory.add_product(product) ##check whether the product is 'physical' or 'digital'


        elif (item['product_type'] == "digital"):
            product = Digital_Product(item["id"], item["name"], item["price"], item["stock_quantity"], item["download size"])
            inventory.add_product(product)
    return inventory

# Load products
def load_products(path: str, inventory: Inventory, supplier: Supplier) -> None:
    loaded = 0
    try:
        file = open(path, newline="")
    except FileNotFoundError:
        print(f"Products file not found: {path}")
    else:
        with file:
            reader = csv.reader(file)
            next(reader, None) # skip the header row
            for row_number, row in enumerate(reader, start=2):
                try:
                    product_type, product_id, name, price, stock = row
                    product = ProductFactory.create(product_type, product_id, name, float(price), int(stock), supplier)
                    inventory.add_product(product)
                    loaded += 1
                except ValueError as error:
                    print(f"Row {row_number} skipped: {error}")
        print(f"{loaded} products loaded.")
    finally:
        print("Load attempt finished.")



def save_inventory(inventory):
    ##Append new transactions to "orders.json", using "a" mode
    order = []

    for product in inventory.get_products():

        orders = {
            "id": product.get_id(), 
            "name": product.get_name(),
            "price": product.get_price(),
            "stock_quantity": product.get_stock()

        }
        if isinstance(product, physical_Product):
            orders["weight"] = product.get_physical_weight()
            orders["product_type"] = "physical"  ##check between 'physical_product' or 'digital_product'

        if isinstance(product,Digital_Product):
            orders["download size"] = product.get_download_size()
            orders["product_type"] = "digital"
    
        order.append(orders)
    
    with open("inventory.json", "w") as file: 
        json.dump(order, file, indent=4)
    print("Saving file..")

def add_product(inventory):

    print("--------Add product-----------")
    id = str(input("Enter an ID: "))
    name= str(input("Enter a product: "))
    ##Reusing code to prompt user for stock quantity
    price = input("Enter the price: ")
    stock_quantity = int(input("Enter a stock quantity: "))
    product_type = input("Enter is it a physical product or digital product: ")

    if (product_type == "physical"):
        value= input("Please enter the weight of this product: ")
        inventory.add_product(physical_Product(id, name, price, stock_quantity, value))

    if(product_type == "digital"):
        value= input("Please enter the download size of the folder: ")
        inventory.add_product(Digital_Product(id, name, price, stock_quantity, value))

    print("Product added successfully! ")


def update_stock(inventory):

    print("-------Update Stock-----------")
    search_id = input("Enter Product ID: ")

    ##Search for product id then update stock
    product = inventory.search_product(search_id)

    if product is None:
            
        print("Product not Found! ")
        return
 
    print("Product Found! ")
    print("Name: ", product.get_name())
    print("Current Stock: ",product.get_stock())
    new_stock = input("New Stock Quantity: ")
    product.update_stock(int(new_stock))
    ##Update stock

    print("Stock updated successfully! ")
  

def search_product(inventory):

    print("----------Search Product------------")
    search_id = input("Enter Product ID: ")
    ##Search for product id then search for list of stock

    product = inventory.search_product(search_id)

    if product is None:
        print("Product not found")

    else: 
        print("Product Found:")
        product.display_product()
