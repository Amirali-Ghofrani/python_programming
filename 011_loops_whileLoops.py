
# refueling the car!:

fuel = 1

if fuel <= 2:
    print("low fuel!")
    while fuel < 10:
        print("fuel:", fuel)
        fuel += 1
    print("fuel:", fuel, "back to the road!")


# gets and prints your name for 5 times

count = 5

while count > 0:
    name = input("please enter your name:")
    print(f"your name is: {name}!\n", sep = "")
    count = count - 1

