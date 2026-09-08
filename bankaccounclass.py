class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")

    def display_balance(self):
        print("Account Holder:", self.name)
        print("Balance:", self.balance)


account1 = BankAccount("Shraddha", 10000)

account1.deposit(5000)
account1.withdraw(3000)
account1.display_balance()