from exercises.fundamentals.src.inheritance.dog import Dog
from exercises.fundamentals.src .inheritance.dalmatian import Dalmatian
from exercises.fundamentals.src.inheritance.bulldog import Bulldog
from exercises.fundamentals.src.inheritance.french_bulldog import FrenchBulldog


def main():
    spot = Dog('Spot')
    perdita = Dalmatian('Perdita')
    meatball = Bulldog('Meatball')
    jacques = FrenchBulldog('Jacques')

    for dog in (spot, perdita, meatball, jacques):
        print(dog.bark())


if __name__ == '__main__':
    main()
