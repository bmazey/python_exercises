def main():

    # a string is an array of characters
    string = "double, double toil and trouble"
    print(string)

    # an integer is on the number line
    dalmatians = 101
    print("number of dalmatians: " + str(dalmatians))

    # a float can represent numbers with decimal places
    money = 2.5
    print("the value of money: " + str(money))

    # casting is the process by which one type is converted into another
    new_money = int(money)
    print("new money: " + str(new_money))

    # using type function
    print(type(dalmatians))

    # casting up (safe)
    dalmatians = float(dalmatians)
    print(dalmatians)

    print(type(dalmatians))

    # let's do booleans?


if __name__ == '__main__':
    main()
