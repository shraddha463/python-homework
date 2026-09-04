shopping = []

while True:
    print("\n1. Add item")
    print("2. View items")
    print("3. Remove item")
    print("0. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        item = input("Enter item: ")
        shopping.append(item)
        print("Item added.")

    elif choice == 2:
        print("Shopping List:")

        for item in shopping:
            print(item)

    elif choice == 3:
        item = input("Enter item to remove: ")

        if item in shopping:
            shopping.remove(item)
            print("Item removed.")
        else:
            print("Item not found.")

    elif choice == 0:
        print("Program ended.")
        break

    else:
        print("Invalid choice.")