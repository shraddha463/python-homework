class Book:
<<<<<<< HEAD
    title = "Python Basics"
    author = "Shraddha"
    price = 500
=======
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
>>>>>>> efe9a5ab1df740e8361c794ca5f42078e7afc85f

    def display(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)
<<<<<<< HEAD


book1 = Book()

book1.display()
=======
        print()


book1 = Book("Python Programming", "John", 500)
book2 = Book("Learn Python", "David", 600)

book1.display()
book2.display()
>>>>>>> efe9a5ab1df740e8361c794ca5f42078e7afc85f
