"""
Some of the functions have a bit cumbersome behavior when we deal with
positional and keyword arguments.

Write a function that accept any iterable of unique values and then
it behaves as range function:


import string


assert = custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']

"""
from typing import Any, Iterable, List


def custom_range(data: Iterable, *args: Any) -> List[Any]:
    """Creating list of iterable's elements. Their order specified in args as element
    for start, element for stop and step. Iterable muct consist of unique values to get
    correct result."""
    if len(args) > 3:
        raise TypeError(f"custom_range expected at most 4 arguments, got {len(args)}")
    if not args:
        return [item for item in data]
    if len(args) == 1:
        result_range = []
        for item in data:
            if item == args[0]:
                break
            result_range.append(item)
        return result_range
    first, last = args[0], args[1]
    step = 1 if len(args) == 2 else args[2]
    if first in data:
        start = data.index(first)
    else:
        return []
    stop = data.index(last) if last in data else None
    if last in data:
        stop = data.index(last)
        return [item for item in data[start:stop:step]]
    return [item for item in data[start::step]]
