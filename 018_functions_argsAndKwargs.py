# if the functions parameters begin with a '*', it will get as many parameters
# that are given to the function as a tuple

def multiply(*my_args):
    result = 1
    for i in my_args:
        result *= i
    return result

print(multiply(5, 2, 4, -3))      # prints -120



# kwargs: 
# similar to args, but makes a dictionary of the arguments

def data(**my_kwargs):
    if "names" in my_kwargs:
        print(f"names are: {my_kwargs["names"]}")
    if "ages" in my_kwargs:
        print (f"ages are: {my_kwargs["ages"]}")



data(names =  ["sara", "joe"], ages = [21, 26])

data (names = ("robbert", "fred"))