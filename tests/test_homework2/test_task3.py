from homework2.task3 import combinations


def test_combinations():
    """Testing geting the right result on short lists."""

    assert combinations([1, 2], [3, 4]) == [
        [1, 3],
        [2, 3],
        [1, 4],
        [2, 4],
    ]


def test_one_element_lists():
    """Testing lists of one elemnt give list of theit elements."""
    assert combinations([1], [2], [3]) == [[1, 2, 3]]


def test_length_of_result():
    """Testing that on longer lists we get the necessary length of result."""
    lst = list(range(5))
    expected_length = len(lst) ** 3
    assert len(combinations(lst, lst, lst)) == expected_length
