"""Task03 - All possible lists"""
from itertools import product
from typing import Any, List


def combinations(*args: List[Any]) -> List[List]:
    """Does all combinations from some lists"""
    return list(map(list, product(*args)))
