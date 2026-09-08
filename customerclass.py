class Customer:
    def __init__(self, customer_id, name, mobile, city):
        self.customer_id = customer_id
        self.name = name
        self.mobile = mobile
        self.city = city

    def display(self):
        print("Customer ID:", self.customer_id)
        print("Name:", self.name)
        print("Mobile Number:", self.mobile)
        print("City:", self.city)


customer1 = Customer(101, "Shraddha", "9876543210", "Basavakalyan")

customer1.display()