

def main():
    # tuples are immutable
    tuple1 = (1, 2, 3)

    # lists are mutable
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

    dictionary = {'hello': 'world', 'weight': 'African or European?'}

    # prints 'world'
    print(dictionary.get('hello'))

    # prints 'African or European?'
    print(dictionary.get('weight'))

    List1 = ['Math', 'Food']
    List1.insert(1,3.2)
    print(List1)

    List2 = ['Hungry', 'Yum']
    List1.extend(List2)
    print(List1)

    List3 = [1.0,1,2,3,5,8,13,21,34,55,89]
    print(sum(List3))


def append_to_sequence(sequence):
    sequence += (9, 9, 9)
    return sequence


if __name__ == '__main__':
    main()
