# how to make a new list containing the values in the existing list multiplied by 2

# conventional method:
list = [0, 1, 2, 3, 4, 5]

new_l = []
for num in list:
    new_l.append(num*2)
print (new_l)

# list comprehension method:

new_l = [ x * 2 for x in list ]
print(new_l)

# combination with "if":
# prints even numbers in the list:

new_l = [x for x in list if x % 2 == 0]
print ("\n",new_l, sep = "")

# "hoop" game!:
hoop = ["hoop!" if n % 3 == 0 else n for n in range(1,20)]
print (hoop)
