def is_even(number):
    return number % 2 == 0


def is_prime(number):
    if number <= 1:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True


def factorial(number):
    result = 1

    for i in range(1, number + 1):
        result = result * i

    return result


def reverse_number(number):
    return int(str(number)[::-1])
