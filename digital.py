from Inheritance_product import Product


class Digital_Product(Product):
        def __init__(self, get_id, get_name, get_stock, update_stock, download_size): 
            super().__init__(get_id, get_name, get_stock, update_stock) ##calling parent
            self._file_download_size = download_size

        def get_download_size(self):
            return (self._file_download_size)

        def display_product(self): 
            super().display_product() ##Extract from infomation from 'parent' 
            print(f"This file has a download of {self._file_download_size} MB!")

        def  get_fulfilment_info(self):
            print("The product is delivered digitally.")