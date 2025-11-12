# sets are an unordered collection of unique elements
# how to define a set:
my_set = {0 , 1}
print((my_set))

# how to define an empty set:
my_set_empty = set()         # dont use set{} cause it initiates an empty dictionary!

# adds a value to a set:
# multiple values cannot be added to a set all at once with .add()
# lists cannot be added to a set
my_set.add(2)
my_set.add("Tehran")
my_set.add(2)              # doesnt cause error, despite sets do not retain identical values
print(my_set)

# sets union:
my_set2 = {0, 1, 2, 3, "Ney York!"}
print(my_set2)
print(my_set.union(my_set2))

# sets intersection:
print(my_set.intersection(my_set2))

# how to assign elements of a list into a set:
animals_list = ["tiger", "eagle", "panda", "horse", "panda", "horse"]
animals_set = set (animals_list)
print(animals_set, type(animals_set))

# another way:
fruits_set = set(["apple", "banana", "orange"])
print(fruits_set, type(fruits_set))