def main():
    # print("This only executes when %s is executed rather than imported" % __file__)

    is_sunny = True
    is_not_sunny = False
    wearing_sunscreen = True
    not_wearing_sunscreen = False

    if is_sunny and wearing_sunscreen:
        print("will we see this?")

    if is_sunny or not_wearing_sunscreen:
        print("how about this?")

    if is_sunny and not_wearing_sunscreen:
        print("looking hot out there ...")
        # return

    if is_not_sunny or not_wearing_sunscreen:
        print("rain, rain go away ...")
        # return

    if not (is_sunny or not wearing_sunscreen):
        print("We won't see this either test!")
        # return

    if (True and True) or (False and False):
        print("success!")

    # ... new examples: let's order food!
    pizza = False
    burgers = False

    if pizza:
        print("let's order pizza!")
    elif burgers:
        print("let's order burgers!")
    else:
        print("actually ... i'm not hungry")


if __name__ == '__main__':
    main()
