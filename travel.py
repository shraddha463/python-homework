class Travel:
    def __init__(self, passenger, source, destination, ticket_price):
        self.passenger = passenger
        self.source = source
        self.destination = destination
        self.ticket_price = ticket_price

    def display(self):
        print("Passenger Name:", self.passenger)
        print("Source:", self.source)
        print("Destination:", self.destination)
        print("Ticket Price:", self.ticket_price)


travel1 = Travel("Shraddha", "Basavakalyan", "Bangalore", 1500)
travel1.display()