"""
Write a function that takes K lists as arguments and returns all possible
lists of K items where the first element is from the first list,
the second is from the second and so one.

You may assume that that every list contain at least one element

Example:

assert combinations([1, 2], [3, 4]) == [
    [1, 3],
    [1, 4],
    [2, 3],
    [2, 4],
]
"""
from typing import Any, List


def combinations(*args: List[Any]) -> List[List]:
    """Giving all possible combinations of lists' elements.
    Create result of first list's elements and add to
    inner list in result element from the next list."""
    first = args[0]
    result = [[item] for item in first]
    temp = []

    for lst in args[1:]:
        for new_item in lst:
            for inner_list in result:
                temp.append(inner_list + [new_item])
        result = temp
        temp = []

    return result
