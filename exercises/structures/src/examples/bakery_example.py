from exercises.structures.src.examples.bakery import Bakery


def add_bakery():
    # print(dir('fox'))
    dominique_ansel = Bakery(['cronut', 'macaroon', 'croissant'])
    print(len(dominique_ansel))

    levain = Bakery(['chocolate chip', 'snickerdoodle', 'oatmeal raisin', 'peanut butter'])
    print(len(levain))

    magnolias = Bakery(['cupcake', 'banana bread'])

    big_bakery = levain + dominique_ansel + magnolias
    print(str(big_bakery.desserts))

    print(levain[0])


if __name__ == '__main__':
    add_bakery()
