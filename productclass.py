class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self):
        total = self.price * self.quantity
        print("Product Name:", self.name)
        print("Price:", self.price)
        print("Quantity:", self.quantity)
        print("Total Price:", total)


product1 = Product("Laptop", 50000, 2)

product1.total_price()