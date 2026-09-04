class Product:
    def __init__(self, product_name, price, quantity):
        self.product_name = product_name
        self.price = price
        self.quantity = quantity

    def display(self):
        print("Product Name:", self.product_name)
        print("Price:", self.price)
        print("Quantity:", self.quantity)


product1 = Product("Laptop", 50000, 2)

product1.display()