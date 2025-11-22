# mapping concept:
def multiply2 (x):                          # gets a parameter and multiplies it by 2
    return x * 2

my_list = [0, 1, 2, 3, 4, 5, 6]
multiplied_2 = map(multiply2, my_list)      # runs 'multiply2' function on every element of my_list
for i in multiplied_2:
    print(i, end = " ")                    # prints elements in 'multiplied_2' 
print()


# naonymous functions('lambda' functions in python)
multiplied_3 = map(lambda x: x * 3, my_list)    # runs the lambda function on every element of my_list
for i in multiplied_3:                          # (gets x and returns x * 3)
    print(i, end = " ")                         # prints elements in 'multiplied_3' 
print()           


# filtering concept:
nums = [0, 1, 2, 5, 6.23, 3.14, 9.56, 10.44]
def floatingNums (x):                          # gets a number and returns True if it's a floating point number
    if x != int(x):
        return True
    return False

my_floats = map(floatingNums, nums)           # runs the 'floatingNums' on each element of my_floats 
for i in my_floats:                          # prints elements in 'my_floats'  
    print(i, end = " ")  
print()           


# using the 'filter' function:                      
filtered_floats = filter(floatingNums, nums)    # retains each element of the list if floatingNums() returns True
print(type(filtered_floats))
filtered_floats_list = list(filtered_floats)
print(filtered_floats_list)


# using the lambda function and filter function
print(list(filter(lambda x: x != int(x), nums)))


# filtering a list and retaining the names which have 4 characters or less using filter() and lambda()
names = ["sara", "david", "anna", "rose", "alex", "robbers", "antony","sam","jenni"] 
filtered_names = filter(lambda x: len(x) <= 4, names)   
print(list(filtered_names))