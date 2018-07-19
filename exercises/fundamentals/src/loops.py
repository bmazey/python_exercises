def main():

    # classic range for loop ... inclusive, exclusive
    for index in range(1, 10):
        # break
        # continue
        print("index: " + str(index))

    # iterative loop
    sentence1 = "the quick brown fox jumps over the lazy dog"

    for character in sentence1:
        print('first loop: ' + character)

    # 'unpacking'
    sentence2 = "the rain in Spain falls mainly on the plain"
    for index, c in enumerate(sentence2):
        print('second loop: ' + c + ' index: ' + str(index))

    sentence3 = "double, double toil and trouble"
    i = 0
    while i < len(sentence3):
        print('third loop: ' + sentence3[i])
        i += 1

    # let's try a mixed type array
    worst_fears = ["spiders", "heights"]

    # let's write a method to sum an array!

    # strings revisited ...
    first = 'cool'
    second = ''
    for c in first:
        second += c
    if first is second:
        print("the strings are the same! " + first + " / " + second)
    else:
        print("the strings are NOT the same! " + first + " / " + second)


if __name__ == '__main__':
    main()
