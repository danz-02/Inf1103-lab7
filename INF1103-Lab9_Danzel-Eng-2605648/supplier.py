class Supplier:

    def __init__(self, id, name, contact_email):
        
        self.__id = id
        self.__name = name
        self.__contact_email = contact_email

        ##refernce as per type hints


    def display_supplier(self):

        print("------------------")
        print("Supplier ID: ", self.__id)
        print("Name: ", self.__name)
        print("Contact Email: ", self.__contact_email)
        print("------------------")


