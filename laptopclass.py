class Laptop:
    def __init__(self, brand, ram, storage, price):
        self.brand = brand
        self.ram = ram
        self.storage = storage
        self.price = price

    def display(self):
        print("Brand:", self.brand)
        print("RAM:", self.ram)
        print("Storage:", self.storage)
        print("Price:", self.price)


laptop1 = Laptop("HP", "8GB", "512GB", 50000)

laptop1.display()