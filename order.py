from Inheritance_product import Product


class OrderLine: 
    def __init__(self, product: Product, quantity: int):
        self.product = product
        self.quantity = quantity

    def calculate_subtotal(self):
        return self.product.get_price() * self.quantity


class Order:
    def __init__(self, order_id: str):
        self.order_id: str = order_id
        self.order_lines: list[OrderLine] = []

    def add_order_line(self, product: Product, quantity: int) -> None:
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

    def remove_order_line(self, product_id: str) -> None:
        for line in self.order_lines:
            if line.product.get_id() == product_id:
                self.order_lines.remove(line)
            return