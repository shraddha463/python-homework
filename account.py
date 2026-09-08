class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def display(self):
        print("Account Holder:", self.name)
        print("Balance:", self.balance)
        print()


account1 = BankAccount("Shraddha", 10000)
account2 = BankAccount("Rahul", 15000)
account3 = BankAccount("Priya", 20000)

account1.display()
account2.display()
account3.display()