class Employee:
    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)
        print("Department:", self.department)
        print()


employee1 = Employee("Rahul", 25000, "IT")
employee2 = Employee("Priya", 30000, "HR")
employee3 = Employee("Amit", 28000, "Sales")
employee4 = Employee("Sneha", 35000, "IT")
employee5 = Employee("Ravi", 27000, "Finance")

employee1.display()
employee2.display()
employee3.display()
employee4.display()
employee5.display()