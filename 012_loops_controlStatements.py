# pass statement acts as a placeholder for further commands:

for letter in "Tehran":
    pass

# break statements finishes the most internal loop:
my_city = ["london", "paris", "tehran", "berlin", "new york", "dallas"]
for city in my_city:
    if city == "tehran":
        print(city, ": this is my beloved home town!")
        break
    else:
        print(city)

# the "continue" statement continues the loop without executing its following lines

grade = [10, 15, 50, 24, 80, 13, 45, 62, 84, 90, 100, 12]
for score in grade:
    if score < 50:
        continue
    print(f"score:{score} passed!")    # only prints passed students
      
