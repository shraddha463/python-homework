class Employee:
    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department

    def display(self):
        print("Employee Name:", self.name)
        print("Salary:", self.salary)
        print("Department:", self.department)


emp1 = Employee("Shraddha", 30000, "IT")

emp1.display()