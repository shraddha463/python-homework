from student import add_student
from result import calculate_total, calculate_percentage, calculate_grade
from validation import validate_name, validate_roll_no, validate_marks


def save_student(student, total, percentage, grade):
    with open("data.txt", "a") as file:
        file.write("Name: " + student["name"] + "\n")
        file.write("Roll No: " + student["roll_no"] + "\n")
        file.write("Marks: " + str(student["marks"]) + "\n")
        file.write("Total: " + str(total) + "\n")
        file.write("Percentage: " + str(percentage) + "\n")
        file.write("Grade: " + grade + "\n")
        file.write("------------------------\n")


name = input("Enter student name: ")
roll_no = input("Enter roll number: ")

marks = []

for i in range(3):
    mark = int(input("Enter marks for subject " + str(i + 1) + ": "))
    marks.append(mark)


if not validate_name(name):
    print("Invalid name")
elif not validate_roll_no(roll_no):
    print("Invalid roll number")
elif not validate_marks(marks):
    print("Invalid marks. Marks must be between 0 and 100.")
else:
    student = add_student(name, roll_no, marks)

    total = calculate_total(marks)
    percentage = calculate_percentage(marks)
    grade = calculate_grade(percentage)

    print("\n--- STUDENT DETAILS ---")
    print("Name:", student["name"])
    print("Roll No:", student["roll_no"])
    print("Marks:", student["marks"])
    print("Total:", total)
    print("Percentage:", percentage)
    print("Grade:", grade)

    save_student(student, total, percentage, grade)

    print("Student data saved successfully.")
