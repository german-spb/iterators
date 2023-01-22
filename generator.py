import types

def flat_generator(list_of_lists):
    cursor_1 = 0
    cursor_2 = 0
    list_result = []
    while cursor_1 < len(list_of_lists):
        while cursor_2 < len(list_of_lists[cursor_1]) - 1:
            a = list_of_lists[cursor_1][cursor_2]
            cursor_2 += 1
            yield a
        a = list_of_lists[cursor_1][cursor_2]
        cursor_2 = 0
        cursor_1 += 1

        yield a

list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
        ]
item = flat_generator(list_of_lists_1)
print(list(item))
# for item in flat_generator(list_of_lists_1):
#     print(item)

def test_2():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test_2()



