"""Test for task01 - Text work"""
from homework2.task03 import combinations


def test_current_combination():
    """Testing that func returns all possible combinations"""
    assert combinations([1, 2], [3, 4]) == [
        [1, 3],
        [1, 4],
        [2, 3],
        [2, 4],
    ]
