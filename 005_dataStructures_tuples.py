# tuples are ordered datastructures similar to lists, but immutable
# how to define a tuple:

my_tuple = (0, 1, 2, 3, "Tehran", "Boston", 3.14)

# other methods used in lists are appliable for tuples as well(except value assignment)

print (my_tuple[4])                   # prints Tehran

# problem: how to define distance between two points:
coordinates = (3,4)
x2 = int(input("x2 = "))
y2 = int(input("y2 = "))
distance = ((x2 - coordinates[0]) **2 + (y2 - coordinates[1]) **2 ) ** 0.5
print("distance = ", distance)