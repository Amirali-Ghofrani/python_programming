class Runner():
    def __init__(self, name):
        self.name = name

    def action(self):
        print(f"{self.name} is running!")


class Boxer():
    def __init__(self, name):
        self.name = name

    def action(self):
        print(f"{self.name} is boxing!")


def status(player):
    player.action()      # action function runs differently based on the object class
    return 0



def main():
    p1 = Runner("James")
    p2 = Boxer("Mike")

    p1.action()           # each action() function is specified to the object class
    p2.action()

    status(p1)
    status(p2)

    return 0


main()