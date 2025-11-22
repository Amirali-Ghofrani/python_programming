# how to define a class:
# creating an object called Book:
# note: 'self' is not a key word and it's just used as a conventional word, it refers to the object
# without using self, our variables would be local and not the object attributes

class Book():
    def getInfo(self, n,p): 
        self.name = n
        self.pages = p

    def printInfo(self):
        print(f"{self.name} has {self.pages} pages!")

my_book = Book()
my_book.getInfo("the book of jungle!", 340)
my_book.printInfo()



# we can use a cunstructor to get called automatically whenever an object is created:
class Car():
    def __init__(self, m = "unknown", color = "unknown"):
        self.model = m
        self.color = color

# now, when an object from class car is created, the init function will run automatically
# (we don't need to call it manually):
# note: we can't have multiple constructors like in cpp, we can use default values instead

my_car = Car("Toyota", "Black")
print(my_car.model, my_car.color)

my_car2 = Car()
print(my_car2.model, my_car2.color)

    