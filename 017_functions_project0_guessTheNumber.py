# a game that the system generates a number and the user should guess it!
# if the user doesn't win, the game restarts and the system generates a new number
# the game continues till the user wins!

import random

def computerNum():       # generates a random number between 1 to 10
    random_number = random.randint(1, 10)
    return random_number

def guess():             # gets a number from the user as the guessed number
    guessed_number = int(input("guess the number! "))
    return guessed_number

def compare(x, y):      # gets 2 numbares and returns true if they are equal
    equal = False
    if x == y:
        equal = True
    return equal


def gameLoop():      # runs the game in a loop until the user wins!
    while 1:
        computer_number = computerNum()
        guessed_number = guess()
        win = compare(computer_number, guessed_number)

        if win == True:
            print("\nCongradulations! You have won!")
            break
        else:
            print(f"Sorry!\n"
                  f"the asnwer: {computer_number}\n"
                  f"the guessed number: {guessed_number}\n"
                  f"No problem! Give another try!\n")
    return 0


def main():
    print ("Hello dear! Welcome to the guess number game!\n"
           "Have fun!\n")
    
    gameLoop()
    return 0


main()