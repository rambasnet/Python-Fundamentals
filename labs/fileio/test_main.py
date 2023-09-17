import main


def test_sort_ascending():
    my_nums = [10, 9, 0. - 6]
    main.sortListInAscendingOrder(my_nums)
    assert (my_nums == [-6, 0, 9, 10])

    # add 3 more test cases


def test_sort_descending():
    my_nums = [0, -10, -1, 5, 100]
    main.sortListInDescendingOrder(my_nums)
    my_nums == [100, 5, 0, -1, -10]

    # add 3 more test cases
