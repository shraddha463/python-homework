age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible to Vote")
else:
    years_left = 18 - age
    print("You have", years_left, "years left to become eligible.")