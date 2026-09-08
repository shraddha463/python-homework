class Laptop:
<<<<<<< HEAD

    def power_on(self):
        print("Laptop is ON")

    def power_off(self):
        print("Laptop is OFF")


laptop1 = Laptop()

laptop1.power_on()
laptop1.power_off()
=======
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
>>>>>>> efe9a5ab1df740e8361c794ca5f42078e7afc85f
