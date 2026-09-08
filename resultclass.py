class Result:
    def __init__(self, name, m1, m2, m3, m4, m5):
        self.name = name
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.m4 = m4
        self.m5 = m5

    def calculate_result(self):
        total = self.m1 + self.m2 + self.m3 + self.m4 + self.m5
        percentage = total / 5

        print("Student Name:", self.name)
        print("Total:", total)
        print("Percentage:", percentage)

        if percentage >= 35:
            print("Result: PASS")
        else:
            print("Result: FAIL")


student1 = Result("Shraddha", 80, 70, 90, 75, 85)

student1.calculate_result()