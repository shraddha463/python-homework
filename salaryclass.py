class Salary:
    def __init__(self, name, basic_salary):
        self.name = name
        self.basic_salary = basic_salary

    def calculate_salary(self):
        hra = self.basic_salary * 20 / 100
        da = self.basic_salary * 10 / 100
        gross_salary = self.basic_salary + hra + da

        print("Employee Name:", self.name)
        print("Basic Salary:", self.basic_salary)
        print("HRA:", hra)
        print("DA:", da)
        print("Gross Salary:", gross_salary)


salary1 = Salary("Shraddha", 30000)

salary1.calculate_salary()