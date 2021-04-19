import pytest

from homework2.task2 import major_and_minor_elem


@pytest.mark.parametrize(
    "lst, expected", [([0, 0, 0, 0, 0, 0], (0, 0)), ([1, 2, 3, 1, 2, 1], (1, 3))]
)
def test_different_lists(lst, expected):
    """Testing that the most common and the least common elements are as expected."""
    assert major_and_minor_elem(lst) == expected
