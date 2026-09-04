class BankAccount:
    def __init__(self, account_holder_name, account_number, balance):
        self.account_holder_name = account_holder_name
        self.account_number = account_number
        self.balance = balance

    def display(self):
        print("Account Holder Name:", self.account_holder_name)
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)


account1 = BankAccount("Shraddha", "1234567890", 25000)

account1.display()