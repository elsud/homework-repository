"""
This task is optional.

Write a generator that takes a number N as an input
and returns a generator that yields N FizzBuzz numbers*
Don't use any ifs, you can find an approach for the implementation in this video**.


Definition of done:
 - function is created
 - function is properly formatted
 - function has tests


>>> list(fizzbuzz(5))
['1', '2', 'fizz', '4', 'buzz']

* https://en.wikipedia.org/wiki/Fizz_buzz
** https://www.youtube.com/watch?v=NSzsYWckGd4
"""
import itertools
from typing import Generator


def fizzbuzz(n: int) -> Generator[str, None, None]:
    """Generating n fizzbuzz numbers without using ifs.

    >>> list(fizzbuzz(5))
    ['1', '2', 'fizz', '4', 'buzz']

    >>> list(fizzbuzz(20))
    ... # doctest: +NORMALIZE_WHITESPACE
    ['1', '2', 'fizz', '4', 'buzz', 'fizz', '7', '8', 'fizz',
    'buzz', '11', 'fizz', '13', '14', 'fizzbuzz', '16', '17',
    'fizz', '19', 'buzz']

    >>> list(fizzbuzz(-10))
    []
    """
    fizzes = itertools.cycle(("", "", "fizz"))
    buzzes = itertools.cycle(("", "", "", "", "buzz"))
    for number in range(1, n + 1):
        yield next(fizzes) + next(buzzes) or str(number)
