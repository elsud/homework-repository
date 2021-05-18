"""
Given a dictionary (tree), that can contains multiple nested structures.
Find_occurrences takes a tree and an element and finds the number of occurrences
of this element in the tree.
Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool
"""
from typing import Any, Iterable


def find_occurrences(tree: dict, element: Any) -> int:
    """Finding the number of occurrences of the element in the tree."""

    def check_dict(dct: dict) -> None:
        """Counting the number of occurrences in the dict."""
        nonlocal counter
        for key, value in dct.items():
            if element == {key: value}:
                counter += 1
                continue

            if isinstance(key, tuple):
                check_sequence(key)
            counter = counter if key != element else counter + 1

            if isinstance(value, dict):
                check_dict(value)
            if isinstance(value, (tuple, set, list)):
                check_sequence(value)
            counter = counter if value != element else counter + 1

    def check_sequence(seq: Iterable) -> None:
        """Counting the number of occurrences in the sequence."""
        nonlocal counter
        for item in seq:
            if isinstance(item, dict):
                check_dict(item)
                continue
            if isinstance(item, (tuple, set, list)):
                check_sequence(item)
            counter = counter if item != element else counter + 1

    counter = 0
    check_dict(tree)
    return counter
