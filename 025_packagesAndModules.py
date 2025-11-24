# pypi.org(python package index) is an official website to seach for python packages

# how to make our own modules and use them:

import myMod                # imports myMod.py file(module) from the current directory
                            # we could also import a single function or variable from a module
                            # like from myMod import my_pi, greet

def getName():              # a function to get the name of the user
    name = input("please enter your name: ")
    return name


def main():
    name = getName()       # runs getName function to get the user's name
    myMod.greet(name)      # calls greet() function from myMod module to greet the user

    number = myMod.poweredBy(2, 7) # calls poweredBy(x, y) function from myMod and returns x powered by x
    print(number)


main()