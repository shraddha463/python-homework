class ShoppingCart:
    def __init__(self, product_name, price, quantity):
        self.product_name = product_name
        self.price = price
        self.quantity = quantity

    def total_bill(self):
        total = self.price * self.quantity

        print("Product Name:", self.product_name)
        print("Price:", self.price)
        print("Quantity:", self.quantity)
        print("Total Bill:", total)


cart1 = ShoppingCart("Shoes", 2000, 2)

cart1.total_bill()