class Student:
    def __init__(self, name, mark1, mark2, mark3):
        self.name = name
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3

    def result(self):
        total = self.mark1 + self.mark2 + self.mark3
        percentage = total / 3

        print("Name:", self.name)
        print("Total:", total)
        print("Percentage:", percentage)


student1 = Student("Shraddha", 80, 75, 90)

student1.result()