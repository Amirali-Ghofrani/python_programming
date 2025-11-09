
# how to define a string in python:

my_str0 = 'be grateful!'
my_str1 = "let's have some fun!"
my_str2 = "01234567"


# indexes in python strings:

my_index0 = my_str0[0]
print(my_index0)                 # prints b

my_index1 = my_str0[-1]        
print(my_index1)                 # prints !


# index slicing:

my_slice = my_str0[3:11]        
print(my_slice)                  # prints grateful

print(my_str2[0:6])              # prints 012345 *6 is not included!


# steps in sclicing
my_slice1 = my_str2[0:6:2]       
print(my_slice1)                 # prints 024

print(my_str2[1:-1])            # prints 123456  * excludes 0 & 7
print(my_str2[1:])              # prints 1234567 * second char to the end
print(my_str2[:-2])             # prints 012345  * first char to -2

print(my_str2[::-1])            # prints 76543210


# how to put new lines(\n) in strings:

# method 1:

my_str3 = """
Hi,
this is a test string!
"""
print(my_str3)

# method 2:
my_str4 = "Hi,\n this is a sample string! \n this is a doublequote: \" \n bye!"
print(my_str4)


# strings are "immutable" objects in python
# how to change a single char in a string:

my_str5 = "amirali"
print(my_str5)

my_str5 = "A" + my_str5[1:]
print(my_str5)

# how to multiply strings!!:
print((my_str5 + " ") * 3)
