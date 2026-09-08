class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print("Area:", 3.14 * self.radius * self.radius)

    def circumference(self):
        print("Circumference:", 2 * 3.14 * self.radius)


circle1 = Circle(5)

circle1.area()
circle1.circumference()