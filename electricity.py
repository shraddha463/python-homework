class ElectricityBill:
    def __init__(self, name, units):
        self.name = name
        self.units = units

    def calculate_bill(self):
        if self.units <= 100:
            bill = self.units * 5

        elif self.units <= 200:
            bill = (100 * 5) + ((self.units - 100) * 7)

        else:
            bill = (100 * 5) + (100 * 7) + ((self.units - 200) * 10)

        print("Customer Name:", self.name)
        print("Units Consumed:", self.units)
        print("Electricity Bill:", bill)


customer1 = ElectricityBill("Shraddha", 250)

customer1.calculate_bill()