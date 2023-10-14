import labs.fileio.file_io as file_io


def test_sort_ascending():
    my_nums = [10, 9, 0. - 6]
    file_io.sortListInAscendingOrder(my_nums)
    assert (my_nums == [-6, 0, 9, 10])

    # add 3 more test cases


def test_sort_descending():
    my_nums = [0, -10, -1, 5, 100]
    file_io.sortListInDescendingOrder(my_nums)
    my_nums == [100, 5, 0, -1, -10]

    # add 3 more test cases
