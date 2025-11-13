# files are another type of variables
# file variables can be manipulated with the command: "open()"

f = open("myfile.txt")
print(type(f))

# reads the file and returns the value as a string, just for once
file = f.read()            # "file" is a string variable now!
print(file, type(file))

# returns nothing for the second time
print(f.read(), -1)

# return f to location 0:
f.seek(0)

# .read() is appliable again:
print(f.read())

# reads only 1 line
f.seek(0)
file2 = f.readline()
print(file2, type(file2))

# reads all lines and returns a list of strings for each line:
f.seek(0)
file3 = f.readlines()
print(file3, type(file3))

# flush and end the process for the file:
f.close()