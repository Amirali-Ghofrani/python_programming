class Book():
    def __init__(self, name, pages):        # class instructor
        print("a new Book created!")
        self.name = name
        self.pages = pages
        print(f"{self.name} has {self.pages} pages")
    
    def __del__(self):                    # class destructor(gets called automatically when the object is deleted)
        print(f"oh! the book {self.name} was removed!")


def main():
    b1 = Book("Hobbit", 4000)
    b2 = Book("the stranger", 120)

    del (b1)                                     # deletes b1 and calls the destructor function
    pause = input("press Enter to continue: ")  # pauses the main function to watch the changes on the terminal
                                              
                                              # when the main function ends, the b2 object also gets deleted automatically
                                             # and calls the destructor
main()

# other double underscor methods(dunders) such as __len__ or __str__ can also be used inside a class