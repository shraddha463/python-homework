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