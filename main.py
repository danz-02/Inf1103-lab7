from Inheritance_product import Product
from physical import physical_Product
from digital import Digital_Product
from inventory import Inventory
from display_information import display_all
from file_handling import load_inventory, add_product, update_stock, search_product, save_inventory

inventory = load_inventory()

while True:

    display_all()
    menu_option = input("Enter your choice: ")

    if menu_option == "1":
        print("Current Inventory: ")
        inventory.display()

    elif menu_option == "2":
        print("Add Product/n")
        add_product(inventory)

    elif menu_option == "3":
        print("Update Product/n")
        update_stock(inventory)

    elif menu_option == "4":
        print("Search Product/n")
        search_product(inventory)

    elif menu_option == "5":
        print("Save Inventory")
        save_inventory(inventory)

    elif menu_option == "6":
        print("Saving inventory before exit...")
        print("Thank you for using Inventory Management System.")
        break
    else:
        print("Invalid choice.. Please try again")
