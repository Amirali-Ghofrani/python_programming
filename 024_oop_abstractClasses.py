# sometimes it's better to define general abstract classes:

class Player():                    # Player is an empty abstract class here
    def __init__(self, name):
        pass

    def jump(self):
        raise NotImplementedError("pls implement the jump!")
    


class Boxer(Player):
    def __init__(self, name):
        Player.__init__(self, name)
        self.name = name

    def jump(self):
        print(f"{self.name} is jumping")
        

# we have created an empty class: Player. all our other classes inherite from
# Player so we can remember to have a name and a jump function specific for each object

def main():
    p1 = Boxer("Mike")
    p1.jump()

main()