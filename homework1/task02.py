"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers,
    and returns if the given sequence is a Fibonacci sequence

We guarantee, that the given sequence contain >= 0 integers inside.

"""
from typing import Sequence, Generator


def _get_fib_seq_generator(start: int) -> Generator:
    """This generator yields the members of fib sequence from start number"""
    fib_seq = [0, 1]
    while True:
        if fib_seq[0] >= start:
            yield fib_seq[0]
        fib_seq[0], fib_seq[1] = fib_seq[1], sum(fib_seq)


def check_fib(data: Sequence[int]) -> bool:
    """Check that sequence is a part of fib sequence.
    Sequence must contain >= 0 integers inside"""
    for elem in zip(_get_fib_seq_generator(data[0]), data):
        if elem[0] != elem[1]:
            return False
    return True