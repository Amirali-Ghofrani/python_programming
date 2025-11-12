# lists are ordered(in contrast to sets and dictionaries) and mutable data structures.
# multiple variable with different types can be stored in a list all at once!

# how to define a list:

my_list0 = [0, 1, 2, 3, 4.2, "Tehran", True]

# all methods of indexing and slicing for strings work for lists as well!

print (my_list0[2])                   # prints 2

print(my_list0[2:])                  #prints [2, 3, 4.2, "London", True]

length = len(my_list0)
print(length)                       # prints 7 (length of my_list0) 
                                    # works for strings as well


# lists can be added together:
my_list1 = [5, 6, "Heidelberg"]
my_list_total = my_list0 + my_list1
print(my_list_total)         

# lists can be multiplied by 2:
print(my_list0 * 2)

# removes the last value from the list and return the removed value:
last_value = my_list0.pop()
print (last_value, "\n", my_list0)

# how to sort a list:
my_list3 = [5, 9, 4, 3, 1, 0, 0, 2, 8 , 1, 2]
my_list3.sort()
print(my_list3)

# removes a value and returns none:
my_list3.remove(my_list3[0])
print(my_list3)

my_list3.remove(1)              # removes the first element which stores value 1
print(my_list3)

# sorts the list in a reversed order:
my_list3.reverse()
print(my_list3)
 
# how to add a value to the end of a list:
my_list3.append(10)
print(my_list3)