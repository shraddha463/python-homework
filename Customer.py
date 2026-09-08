class Customer:

    def show_customer(self):
        print("Customer details displayed")

    def place_order(self):
        print("Order placed successfully")

    def cancel_order(self):
        print("Order cancelled successfully")


customer1 = Customer()

customer1.show_customer()
customer1.place_order()
customer1.cancel_order()