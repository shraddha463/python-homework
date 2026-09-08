class car:
    def __init__(self, company, model, price):
        self.company = company
        self.model = model
        self.price = price

    def display(self):
        print("company Name:", self.company)
        print("model:", self.model)
        print("price:", self.price)


car1 = car("Toyota", "Fortuner", 4000000)

car1.display()