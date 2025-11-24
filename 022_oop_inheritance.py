# comprehension of the inheritance concept in oop

class Book():
    def __init__(self, name, pages):
        self.name = name
        self.pages = pages

    def open(self):
        print(f"opened {self.name} which has {self.pages} pages")


class MedicalBook(Book):                        # a subclass which inherits features from class Book
    def __init__(self, subspecialty, level, name, pages):
        Book.__init__(self, name, pages)
        print("a new medical book!")
        self.subsp = subspecialty
        self.level = level
     
    def open(self):
        print(f"opened {self.name}, a {self.subsp} medical book for {self.level}"
              f" students which has {self.pages} pages")
    

def main():
    my_book1 = Book("LOTR", 3000)
    my_book1.open()

    my_book2 = MedicalBook("psychiatry", "PGY-2", "Kaplan", "2000")  # inherites name and pages from class Book
    my_book2.open()                                                 # runs 'open' function of the MedicalBook class
    

main()
    
