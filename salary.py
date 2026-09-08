class Employee:
    def __init__(self, name, monthly_salary):
        self.name = name
        self.monthly_salary = monthly_salary

    def annual_salary(self):
        annual = self.monthly_salary * 12

        print("Name:", self.name)
        print("Monthly Salary:", self.monthly_salary)
        print("Annual Salary:", annual)


emp1 = Employee("Shraddha", 30000)

emp1.annual_salary()