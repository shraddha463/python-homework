class Product:
<<<<<<< HEAD
    name = "Laptop"
    price = 50000
    quantity = 2

    def display(self):
        print("Product Name:", self.name)
=======
    def __init__(self, product_name, price, quantity):
        self.product_name = product_name
        self.price = price
        self.quantity = quantity

    def display(self):
        print("Product Name:", self.product_name)
>>>>>>> efe9a5ab1df740e8361c794ca5f42078e7afc85f
        print("Price:", self.price)
        print("Quantity:", self.quantity)


<<<<<<< HEAD
product1 = Product()
=======
product1 = Product("Laptop", 50000, 2)
>>>>>>> efe9a5ab1df740e8361c794ca5f42078e7afc85f

product1.display()