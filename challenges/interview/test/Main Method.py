
class Life:
    def __init__(self,name):
        # set a self name so that we can customize the name of objects used later on.
        self.name = name

    def eat(self):
        # now giving class Human an attribute
        print(self.name + " " + "needs to eat to survive")

    def sleep(self):
        print(self.name + " " + "needs to sleep to work efficiently")


def main():
    # we now define a main method to combine all attributes mentioned above
    diana = Life("Diana")
    # we create an object called "Diana"
    diana.eat()
    diana.sleep()


if __name__ == "__main__":
    main()


