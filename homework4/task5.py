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
from typing import Generator


def fizzbuzz(n: int) -> Generator[str, None, None]:
    """Generating n fizzbuzz numbers without using ifs. N must be a natural number.

    >>> list(fizzbuzz(5))
    ['1', '2', 'fizz', '4', 'buzz']

    >>> list(fizzbuzz(20))
    ... # doctest: +NORMALIZE_WHITESPACE
    ['1', '2', 'fizz', '4', 'buzz', 'fizz', '7', '8', 'fizz',
    'buzz', '11', 'fizz', '13', '14', 'fizzbuzz', '16', '17',
    'fizz', '19', 'buzz']

    >>> list(fizzbuzz(0))
    []
    """
    first_15 = dict.fromkeys((1, 2, 4, 7, 8, 11, 13, 14), " ")
    first_15.update(dict.fromkeys((3, 6, 9, 12), "fizz"))
    first_15.update(dict.fromkeys((5, 10), "buzz"))
    first_15[15] = "fizzbuzz"
    counter = 1
    for _ in range(n // 15):
        for i in range(1, 16):
            yield first_15[i].replace(" ", f"{str(counter)}")
            counter += 1
    for i in range(1, n % 15 + 1):
        yield first_15[i].replace(" ", f"{str(counter)}")
        counter += 1
