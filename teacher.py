class Teacher:
    name = "Priya"
    subject = "Python"
    experience = 5

    def display_details(self):
        print("Teacher Name:", self.name)
        print("Subject:", self.subject)
        print("Experience:", self.experience, "years")


teacher1 = Teacher()

teacher1.display_details()