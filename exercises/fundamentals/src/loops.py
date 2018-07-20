def main():

    # classic range for loop ... inclusive, exclusive
    for index in range(1, 10):
        # break
        # continue
        print("index: " + str(index))
        # return

    # iterative loop
    sentence1 = "the quick brown fox jumps over the lazy dog"

    for index in sentence1:
        print('first loop: ' + index)
        # return

    # 'unpacking'
    sentence2 = "the rain in Spain falls mainly on the plain"
    for index, c in enumerate(sentence2):
        print('second loop: ' + c + ' index: ' + str(index))
        # return

    sentence3 = "double, double toil and trouble"
    i = 0
    while i < len(sentence3):
        print('third loop: ' + sentence3[i])
        i += 1

    # let's try a mixed type array
    worst_fears = ['spiders', 'heights', 'blood', 13, 4.56989876]
    for fear in worst_fears:
        print("my fears: " + str(fear))

    # let's write a method to sum an array!

    # strings revisited ...
    first = 'cool'
    second = 'cool'
    # for c in first:
        # second += c
    if first is second:
        print("the strings are the same! " + first + " / " + second)
    else:
        print("the strings are NOT the same! " + first + " / " + second)


def sum_array(mylist):
    result = 0
    for c in mylist:
        result += c
    return result


if __name__ == '__main__':
    main()
    # test = [2, 4, 6]
    # print(sum_array(test))
