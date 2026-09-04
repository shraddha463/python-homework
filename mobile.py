class Mobile:
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