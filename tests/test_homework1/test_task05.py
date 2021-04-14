from homework1.task05 import find_maximal_subarray_sum


def test_sum_of_long_array():
    """Testing that sum of subarray is counted correctly."""
    assert find_maximal_subarray_sum([1, 3, -1, -3, 5, 3, 6, 7], 3) == 16


def test_sum_of_subarray_longer_than_array():
    """Testing that subarray longer than array gives sum of array."""
    arr = [1, -12, 5, 78, 0]
    assert find_maximal_subarray_sum(arr, 7) == sum(arr)


def test_sum_of_empty_array():
    """Testing that sum of subarray of empty array gives zero."""
    assert find_maximal_subarray_sum([], 3) == 0
