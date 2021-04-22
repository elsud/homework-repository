from homework1.task04 import check_sum_of_four


def test_empty_lists():
    """Testing that empty lists give zero."""
    check_sum_of_four([], [], [], []) == 0


def test_zero_lists():
    """Testing that lists consisting of zeroes give len of decart product of all elements."""
    arr = [0, 0, 0]
    check_sum_of_four(arr, arr, arr, arr) == len(arr) ** 4
