class Laptop:
    def __init__(self, brand, ram, processor, price):
        self.brand = brand
        self.ram = ram
        self.processor = processor
        self.price = price

    def display(self):
        print("Brand:", self.brand)
        print("RAM:", self.ram)
        print("Processor:", self.processor)
        print("Price:", self.price)


laptop1 = Laptop("HP", "8GB", "Intel i5", 55000)

laptop1.display()