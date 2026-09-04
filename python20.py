while True:
    print("\n1. Say Hello")
    print("2. Say Welcome")
    print("0. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Hello!")

    elif choice == 2:
        print("Welcome!")

    elif choice == 0:
        print("Program ended.")
        break

    else:
        print("Invalid choice.")