class Product:
    name = "Laptop"
    price = 50000
    quantity = 2

    def display(self):
        print("Product Name:", self.name)
        print("Price:", self.price)
        print("Quantity:", self.quantity)


product1 = Product()

product1.display()