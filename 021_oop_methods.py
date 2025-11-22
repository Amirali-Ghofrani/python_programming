class Circle():                         # creates a class called Circle
    pi = 3.1415926

    def __init__(self, r):
        self.r = r
        
    def area(self):
        ar = Circle.pi * self.r * self.r     # we can also use 'self.pi' here
        return ar
    
    def circumference(self):
        cir = 2 * self.pi * self.r
        return cir
    
def main():
    c1 = Circle(5)                     # initiates an object from the class Circle, gets a parameter as the circle radius
    print(c1.area())                   # uses class methods to calculate c1 area and circumference
    print(c1.circumference())

main()