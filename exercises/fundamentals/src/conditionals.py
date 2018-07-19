def main():
    # print("This only executes when %s is executed rather than imported" % __file__)

    is_sunny = True
    is_not_sunny = False
    wearing_sunscreen = True
    not_wearing_sunscreen = False

    if is_sunny and wearing_sunscreen:
        print("will we see this?")

    if is_sunny or wearing_sunscreen:
        # print("how about this?")
        return

    if is_sunny and not_wearing_sunscreen:
        # print("looking hot out there ...")
        return

    if is_not_sunny or not_wearing_sunscreen:
        # print("rain, rain go away ...")
        return

    if not is_sunny or not wearing_sunscreen:
        # print("We won't see this either!")
        return

    # ... new examples: let's order food!
    pizza = False
    burgers = True

    if pizza:
        # print("let's order pizza!")
        return
    elif burgers:
        # print("let's order burgers!")
        return
    else:
        # print("actually ... i'm not hungry")
        return


if __name__ == '__main__':
    main()
