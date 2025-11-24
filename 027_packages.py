# to have a package, we make a directory and creat a file called '__init__py' inside it,
# so that python can see it as a package
# we can have multiple modules in our package and import them into our main programm

from jackage.variables import pi
from jackage.myMath import cirArea, cir
import jackage.game

def getRadius():          # gets the circle radius from the user
    r = int(input("enter the radius of your circle: "))
    return r

def getHoop():           # gets x and hoop from the user for the hoopGame
    x, y = input("please enter x: \n"), input("please enter hoop: \n")
    return x, y



def main():
    radius = getRadius()
    circum = cir(radius, pi)                # uses cir() and cirArea() from the 'jackage' package! to 
    area = cirArea(radius, pi)             # calculate circle circumference and area

    print(f"circumference is: {circum}\n"
          f"area is: {area}")                   # prints the resulta
    
    game = input("enter y if you wanna play hoop!: ")  # asks if the user wants to play hoop game
    if game == 'y':
        x, hoop = getHoop()
        result = jackage.game.hoopGame(x, hoop)      # uses the game module inside jackage to 
        print(result)                                # run the hoop game



main()

