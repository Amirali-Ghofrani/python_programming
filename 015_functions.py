# how to define a function in python:

def helloWorld():
    print("Hello World!")
    return 0                  # 'return 0' is not necessarily needed in python, but it's c++ style! :-D

                          
def askName():               # gets name of the user and returns it as a string
    name = input("Hi, What's your name? ")
    return name


def helloName(name, n = 1):           # gets a string and an int as parameters, prints the given string for n times. also
    for i in range (n):               # the function sets the default value for n to 1, unless it is given another value when 
        print(f"Hello dear {name}!")  # the function is called
    return 0

# it's better to define a main function and call other functions inside the main(c++ style!)
def main():

    helloWorld()        # calling helloWorld function inside the main
    name = askName()
    helloName(name, 5)  # also can be written as helloName(name, n = 5)

    return 0


main()              # calling the main function

# function parameters are dynamic type in python, so they can deffer in type(int,
      