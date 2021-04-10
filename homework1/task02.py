"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers,
    and returns if the given sequence is a Fibonacci sequence

We guarantee, that the given sequence contain >= 0 integers inside.

"""
from typing import Sequence


def _get_fib_seq(end: int) -> Sequence[int]:
    """return the part of fib sequence from 0 to end"""
    fib_seq = [0, 1]
    while fib_seq[-1] < end:
        fib_seq.append(fib_seq[-2] + fib_seq[-1])
    return fib_seq


def check_fib(data: Sequence[int]) -> bool:
    """Check that sequence is a part of fib sequence"""
    max_seq_value = data[-1]
    if max_seq_value < 0:
        return False
    if len(data) == 1 and data[0] in (0, 1) or len(data) == 2 and data == [1, 1]:
        return True

    fib_seq = _get_fib_seq(max_seq_value)
    return fib_seq[-len(data) :] == data
