# for loops can be manipulated in iterable objects:

my_list = [0, 1, 2, 3, "Tehran"]

for my_item in my_list:
    print(f"my item is: {my_item}\n")
    if my_item == "Tehran":
        print("Welcome to my beautiful Tehran! :-D <3")

print("\n\nthe first for loop ended!\n")


# we can use "_" as a for variable to show we do not need the variable itself(just to increase readability):
count = 0
for _ in my_list:
    count = count + 1
print(f"count = {count}\n\n")


# for loops can also be used to iterate strings, tuples and other iterable objects

# iteration and unpacking in tuples:
my_tuple = (("sara", 45), ("erward", 22), ("frank", 43))
for name, age in my_tuple:
    print(f"name: {name}\n age: {age}")
print("\n\n")
    

# iteration and unpacking in dictionaries:

my_dictionary = {"sara":(45, 180), "edward": (22, 170), "frank": (43, 190)}
for person in my_dictionary:
    print(person)                     # only prints the keys!   
print("\n\n")

# a method to print also the values:

for person in my_dictionary:
    print(" name:", person,                            # prints the key         
          " age:", my_dictionary[person][0],           # prints index 0 of the value
          " height:", my_dictionary[person][1])        # prints index 1 of the value
print("\n\n")
    
# another way:
for persons in my_dictionary.items():
    print(persons)
print("\n\n")

# another way:
for names, data in my_dictionary.items():
    print(names, data)

# reminder: dictionaries are not ordered structures!



