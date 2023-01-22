class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.cursor_1 = 0
        self.cursor_2 = 0
        return self

    def __next__(self):
        if self.cursor_1 < len(self.list_of_list):
            if self.cursor_2 < len(self.list_of_list[self.cursor_1])-1:
                self.a = self.list_of_list[self.cursor_1][self.cursor_2]
                self.cursor_2 += 1
            else:
                self.a = self.list_of_list[self.cursor_1][self.cursor_2]
                self.cursor_2 = 0
                self.cursor_1 += 1


        else:
            raise StopIteration

        return self.a
#
list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

print(list(FlatIterator(list_of_lists_1)))

def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()