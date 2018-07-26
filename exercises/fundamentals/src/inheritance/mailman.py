from exercises.fundamentals.src.inheritance.dog import Dog
from exercises.fundamentals.src .inheritance.dalmatian import Dalmatian
from exercises.fundamentals.src.inheritance.bulldog import Bulldog
from exercises.fundamentals.src.inheritance.french_bulldog import FrenchBulldog

# The below shows how you use a 'nonstatic method' to generate new name.
# A static method makes all instances under the class where it is have the same conditions.
# A nonstatic method allows you to customize the properties of instances in the same class.


def main():
    print(Dog.walk())
    dog1 = Dog('spot')
    print("original name: " + dog1.name)
    # "+ dog1.name" is used to add the old & new names onto the final result

    dog1.rename('Lassy')
    # here we use a rename method to give a new name to dog1. dog1 is just a placeholder, which means it can be changed
    # into any other words

    print("new name: " + dog1.name)

    perdita = Dalmatian('Perdita')
    meatball = Bulldog('Meatball')
    jacques = FrenchBulldog('Jacques')

    for dog in (dog1, perdita, meatball, jacques):
        print(dog.bark())
        print(dog.name)

    print(FrenchBulldog.walk())

    # name clashing! Python methods are simply variables that can be invoked!
    # print(meatball.size())

    # property method!
    jacques.collar = 'yellow'
    print("jacques collar: " + jacques.collar)

    # everything is an object!!
    print(dir(2))


if __name__ == '__main__':
    main()
