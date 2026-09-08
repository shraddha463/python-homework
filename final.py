class Product:
    def __init__(self, name, price, discount):
        self.name = name
        self.price = price
        self.discount = discount

    def calculate_price(self):
        discount_amount = self.price * self.discount / 100
        final_price = self.price - discount_amount

        print("Product Name:", self.name)
        print("Original Price:", self.price)
        print("Discount:", self.discount, "%")
        print("Final Price:", final_price)


product1 = Product("Laptop", 50000, 10)

product1.calculate_price()