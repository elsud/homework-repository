"""Test for task02_var2 - Most&least common"""
import pytest

from homework2.task02_var2 import major_and_minor_elem


def test_correct_input_for_counting():
    """Testing right input"""
    assert major_and_minor_elem([1, 1, 2]) == 1, 2


@pytest.mark.parametrize(
    "my_input, output",
    [
        (
            [1, 1, 1, 2, 2, 3],
            input(
                "There is not element, which fills list more than n//2. "
                "Please, input right list "
            ).split(),
        ),
        (
            [1, 1, 2, 3],
            input(
                "More than 1 element is the least common. Please, input right list "
            ).split(),
        ),
    ],
)
def test_incorrect_input_for_counting(my_input, output):
    """Testing wrong input"""
    assert major_and_minor_elem(my_input) == output
