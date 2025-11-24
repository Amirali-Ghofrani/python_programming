# my sample functions:

my_pi = 3.1415

def greet(name):
    print(f"Hello dear {name}!, Happy to see you here!")
    return 0

def poweredBy(x, y):    # gets 2 arguments x & y and returns x powered by y
    holder = 1
    for i in range (y):
        holder = holder * x
    return holder

