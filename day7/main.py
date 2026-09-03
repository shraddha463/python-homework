# # # # # import calculator
# # # # # print("Addition:", calculator.add(10,5))
# # # # # print("subtraction",calculator.subtract(10,5))
# # # # # print("multiplication",calculator.multiplication(10,5))
# # # # # print("division",calculator.division(10,5))

# # # # # from message import welcome
# # # # # welcome()

# # # # # from student import student_info
# # # # # student_info("shraddha",20,"python")

# # # # # from greeting import hello
# # # # # hello()

# # # # # from temperature import (
# # # # #     celsius_to_fahrenheit,
# # # # #     fahrenheit_to_celsius
# # # # # )

# # # # # print("Celsius to Fahrenheit:", celsius_to_fahrenheit(25))
# # # # # print("Fahrenheit to Celsius:", fahrenheit_to_celsius(77))

# # # # # import math
# # # # # number=5
# # # # # print("square root:", math.sqrt(number))
# # # # # print("factorial:", math.factorial(number))
# # # # # print("power:",math.pow(number,2))

# # # # # import random
# # # # # number=random.randint(1,100)
# # # # # print("random number:",number)

# # # # # import random
# # # # # fruits=["apple", "banana", "mango","orange"]
# # # # # choice =random.choice(fruits)
# # # # # print("random fruits:", choice)

# # # # # import random
# # # # # number=random.randint(10,50)
# # # # # print("Random number:",number)

# # # # # import random
# # # # # numbers=[1,2,3,4,5]
# # # # # random.shuffle(numbers)
# # # # # print("shuffled list:",numbers)

# # # # # import datetime

# # # # # current_datetime = datetime.datetime.now()

# # # # # print("Current date and time:", current_datetime)
# # # # # import calculator

# # # # # while True:
# # # # #     print("\n--- CALCULATOR ---")
# # # # #     print("1. Addition")
# # # # #     print("2. Subtraction")
# # # # #     print("3. Multiplication")
# # # # #     print("4. Division")
# # # # #     print("5. Exit")

# # # # #     choice = input("Enter your choice: ")

# # # # #     if choice == "5":
# # # # #         print("Calculator closed.")
# # # # #         break

# # # # #     a = float(input("Enter first number: "))
# # # # #     b = float(input("Enter second number: "))

# # # # #     if choice == "1":
# # # # #         print("Result:", calculator.add(a, b))

# # # # #     elif choice == "2":
# # # # #         print("Result:", calculator.subtract(a, b))

# # # # #     elif choice == "3":
# # # # #         print("Result:", calculator.multiply(a, b))

# # # # #     elif choice == "4":
# # # # #         print("Result:", calculator.divide(a, b))

# # # # #     else:
# # # # #         print("Invalid choice")

# # # # # from student import calculate_total, calculate_percentage, calculate_grade

# # # # # marks = [85, 78, 92, 88, 80]

# # # # # total = calculate_total(marks)

# # # # # percentage = calculate_percentage(marks)

# # # # # grade = calculate_grade(percentage)

# # # # # print("Total marks:", total)
# # # # # print("Percentage:", percentage)
# # # # # print("Grade:", grade)
# # # # from employee import employee_details, calculate_salary

# # # # name = input("Enter employee name: ")
# # # # employee_id = input("Enter employee ID: ")

# # # # basic_salary = float(input("Enter basic salary: "))
# # # # bonus = float(input("Enter bonus: "))

# # # # print("\n--- Employee Details ---")

# # # # employee_details(name, employee_id)

# # # # total_salary = calculate_salary(basic_salary, bonus)

# # # # print("Total Salary:", total_salary)
# # # from bank import deposit, withdraw, check_balance

# # # while True:

# # #     print("\n--- BANK MENU ---")
# # #     print("1. Deposit")
# # #     print("2. Withdraw")
# # #     print("3. Check Balance")
# # #     print("4. Exit")

# # #     choice = input("Enter your choice: ")

# # #     if choice == "1":
# # #         amount = float(input("Enter deposit amount: "))

# # #         result = deposit(amount)

# # #         print("Amount deposited successfully.")
# # #         print("Current balance:", result)

# # #     elif choice == "2":
# # #         amount = float(input("Enter withdrawal amount: "))

# # #         result = withdraw(amount)

# # #         print("Result:", result)

# # #     elif choice == "3":
# # #         print("Current balance:", check_balance())

# # #     elif choice == "4":
# # #         print("Thank you for using the bank!")
# # #         break

# # #     else:
# # #         print("Invalid choice")
# # from authentication import register_user, login_user


# # while True:

# #     print("\n--- LOGIN SYSTEM ---")
# #     print("1. Register")
# #     print("2. Login")
# #     print("3. Exit")

# #     choice = input("Enter your choice: ")

# #     if choice == "1":

# #         username = input("Enter username: ")
# #         password = input("Enter password: ")

# #         result = register_user(username, password)

# #         print(result)

# #     elif choice == "2":

# #         username = input("Enter username: ")
# #         password = input("Enter password: ")

# #         result = login_user(username, password)

# #         print(result)

# #     elif choice == "3":

# #         print("Thank you!")
# #         break

# #     else:

# #         print("Invalid choice")
# from cart import add_product, remove_product, calculate_total, display_cart


# while True:

#     print("\n--- SHOPPING CART MENU ---")
#     print("1. Add Product")
#     print("2. Remove Product")
#     print("3. Display Cart")
#     print("4. Calculate Total")
#     print("5. Exit")

#     choice = input("Enter your choice: ")

#     if choice == "1":

#         product = input("Enter product name: ")
#         price = float(input("Enter product price: "))

#         add_product(product, price)

#         print("Product added successfully")

#     elif choice == "2":

#         product = input("Enter product name: ")

#         print(remove_product(product))

#     elif choice == "3":

#         display_cart()

#     elif choice == "4":

#         total = calculate_total()

#         print("Total amount:", total)

#     elif choice == "5":

#         print("Thank you for shopping!")
#         break

#     else:

#         print("Invalid choice")
from utilities.calculator import add, subtract, multiply, divide
from utilities.student import calculate_total, calculate_percentage, calculate_grade
from utilities.employee import employee_details, calculate_salary


print("--- CALCULATOR ---")

print("Addition:", add(10, 5))
print("Subtraction:", subtract(10, 5))
print("Multiplication:", multiply(10, 5))
print("Division:", divide(10, 5))


print("\n--- STUDENT RESULT ---")

marks = [85, 78, 92, 88, 80]

total = calculate_total(marks)
percentage = calculate_percentage(marks)
grade = calculate_grade(percentage)

print("Total marks:", total)
print("Percentage:", percentage)
print("Grade:", grade)


print("\n--- EMPLOYEE ---")

print(employee_details("Shraddha", "101"))

salary = calculate_salary(20000, 5000)

print("Total salary:", salary)