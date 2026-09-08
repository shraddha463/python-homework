class Mobile:
<<<<<<< HEAD
    def call(self):
        print("Calling...")

    def message(self):
        print("Message sent")


mobile1 = Mobile()

mobile1.call()
mobile1.message()
=======
    def __init__(self, company, model, price):
        self.company = company
        self.model = model
        self.price = price

    def display(self):
        print("Company:", self.company)
        print("Model:", self.model)
        print("Price:", self.price)
        print()


mobile1 = Mobile("Samsung", "Galaxy S24", 70000)
mobile2 = Mobile("Apple", "iPhone 15", 60000)
mobile3 = Mobile("OnePlus", "12R", 45000)

mobile1.display()
mobile2.display()
mobile3.display()
>>>>>>> efe9a5ab1df740e8361c794ca5f42078e7afc85f
