students = []

while True:
    print("\n===== Student Management =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Remove Student")
    print("0. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter student name: ")
        students.append(name)
        print("Student added successfully.")

    elif choice == 2:
        if len(students) == 0:
            print("No students found.")
        else:
            print("\nStudent List:")

            for student in students:
                print(student)

    elif choice == 3:
        name = input("Enter student name to remove: ")

        if name in students:
            students.remove(name)
            print("Student removed successfully.")
        else:
            print("Student not found.")

    elif choice == 0:
        print("Program ended.")
        break

    else:
        print("Invalid choice.")