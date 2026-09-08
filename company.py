class Company:
    name = "real Technologies"
    location = "Bangalore"
    employees = 100

    def company_details(self):
        print("Company Name:", self.name)
        print("Location:", self.location)
        print("Employees:", self.employees)


company1 = Company()

company1.company_details()