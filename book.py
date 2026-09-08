class Book:
    title = "Python Basics"
    author = "Shraddha"
    price = 500

    def display(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)


book1 = Book()

book1.display()