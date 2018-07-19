def main():
    print("This only executes when %s is executed rather than imported" % __file__)

    is_sunny = True
    is_not_sunny = False
    wearing_sunscreen = True
    not_wearing_sunscreen = False

    if is_sunny and wearing_sunscreen:
        print("This is true!")

    if is_sunny or wearing_sunscreen:
        print("This is also true!")

    if is_sunny and not_wearing_sunscreen:
        print("Don't think we'll see this ...")

    if (is_not_sunny or not_wearing_sunscreen) or (True and True):
        print("We won't see this!")

    if not is_sunny or not wearing_sunscreen:
        print("We won't see this either!")

    # ... new examples: let's order food!
    pizza = False
    burgers = True

    if pizza:
        print("let's order pizza!")
    elif burgers:
        print("let's order burgers!")
    else:
        print("actually ... i'm not hungry")


if __name__ == '__main__':
    main()
