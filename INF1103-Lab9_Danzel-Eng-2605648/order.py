from Inheritance_product import Product
from product_factory import DiscountStrategy

class OrderLine: 
    def __init__(self, product: Product, quantity: int):
        self.product = product

        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        self.quantity = quantity

    def calculate_subtotal(self):
        return self.product.get_price() * self.quantity

class Order:
    def __init__(self, order_id: str, discount: DiscountStrategy):
        self.order_id: str = order_id
        self.order_lines: list[OrderLine] = []

        if discount is None:
            self.discount: DiscountStrategy = NoDiscount() ##to do a check if the product is 'Discount eligible'
        else:
            self.discount: DiscountStrategy = discount

    def add_order_line(self, product: Product, quantity: int) -> None:
        ##add exsisting products into inventory
        order_line = OrderLine(product, quantity)
        self.order_lines.append(order_line)


    def display_order(self) -> None:
        print("------------------")
        print("Order ID: ", self.order_id)
        total = 0
        for line in self.order_lines:
            subtotal = line.calculate_subtotal()
            total += subtotal
            print("Product Name: ", line.product.get_name())
            print("Quantity: ", line.quantity)
            print("Subtotal: ", line.calculate_subtotal())
        print("------------------")

    def remove_order_line(self, product_id: str):
        ##remove orders line with references to 'product_id'
        for line in self.order_lines:
            if line.product.get_id() == product_id:
                self.order_lines.remove(line)
            return

    def set_discount(self, discount: DiscountStrategy):
        self.discount = discount

    def calculate_total(self):
        total = sum(line.calculate_subtotal() for line in self.order_lines)
        return self.discount.apply(total)

