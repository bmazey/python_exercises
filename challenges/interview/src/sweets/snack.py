from challenges.interview.src.sweets.dessert import Dessert
from challenges.interview.src.sweets.cookie import Cookie
from challenges.interview.src.sweets.brownie import Brownie


def main():
    sweets = Dessert('cookies')
    print(sweets.name)

    savory = Dessert('brownie')
    print(savory.get_dessert_name())

    macaroon = Cookie('coconut')
    print(macaroon.get_dessert_name())

    brownie = Brownie('fudge', 5)
    print(brownie.get_brownie_size())

    for dessert in (sweets, savory, macaroon, brownie):
        print(dessert.name)


if __name__ == '__main__':
    main()

