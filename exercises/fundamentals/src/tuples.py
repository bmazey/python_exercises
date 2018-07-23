import time

def main():

    # tuples are ordered and immutable
    # heterogeneous data structures (i.e., their entries have different meanings)
    # tuples (generally) are sequences of different kinds of stuff, and you deal with the tuple as a coherent unit
    tuple1 = (1, 2, 3)

    # lists are mutable
    # ordered homogeneous sequences
    # lists (generally) are sequences of the same kind of stuff, and you deal with the items individually.
    list1 = [1, 2, 3]

    tuple2 = append_to_sequence(tuple1)
    list2 = append_to_sequence(list1)

    # outputs (1, 2, 3)
    print('tuple1 = ', tuple1)

    # outputs (1, 2, 3, 9, 9, 9)
    print('tuple2 = ', tuple2)

    # outputs [1, 2, 3, 9, 9, 9]
    print('list1 = ', list1)

    # outputs [1, 2, 3, 9, 9, 9]
    print('list2 = ', list2)

    # direct access on immutable
    # tuple1[0] = 4
    list1[0] = 4
    # print("new list1 = " + str(list1))

    dictionary = {'hello': 'world', 'weight': 'African or European?'}

    # prints 'world'
    print(dictionary.get('hello'))

    # prints 'African or European?'
    print(dictionary.get('weight'))

    # tuples with enumeration
    quote = "know thy self, know thy enemy. A thousand battles, a thousand victories."
    # print(list(enumerate(quote)))
    # print(list(enumerate(quote.split(' '))))

    # tuple example
    # time.localtime()
    print(time.localtime())


def append_to_sequence(sequence):
    sequence += (9, 9, 9)
    return sequence


if __name__ == '__main__':
    main()
