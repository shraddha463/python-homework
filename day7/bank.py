balance = 0


def deposit(amount):
    global balance
    balance = balance + amount
    return balance


def withdraw(amount):
    global balance

    if amount > balance:
        return "Insufficient balance"

    balance = balance - amount
    return balance


def check_balance():
    return balance