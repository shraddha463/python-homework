class Movie:
    name = "3 Idiots"
    actor = "Aamir Khan"
    actress = "Kareena Kapoor"
    rating = 4.5

    def display(self):
        print("Movie Name:", self.name)
        print("Actor:", self.actor)
        print("Actress:", self.actress)
        print("Rating:", self.rating)


movie1 = Movie()

movie1.display()