# how to define a class:
# creating an object called Book:

class Book():
    def getInfo(self, n,p):
        self.name = n
        self.pages = p

    def printInfo(self):
        print(f"{self.name} has {self.pages} pages!")

my_book = Book()
my_book.getInfo("the book of jungle!", 340)
my_book.printInfo()



# we can use a cunstructor to be called automatically whenever an object is created:
class Car():
    def __init__(self, model, color):
        self.model = model
        self.color = color

# now, when an object from class car is created, the init function will run automatically
# (we don't need to call it manually):

my_car = Car("Toyota", "Black")
print(my_car.model, my_car.color)

    