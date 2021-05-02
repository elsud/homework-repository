"""Tests for task04 - Cache"""
from homework2.task04 import cache

counter = 0


def test_cache_decorator():
    """Testing that func returns values from cache
    if arguments from cacheable func repeats"""

    @cache
    def func(*args):
        global counter
        counter += 1
        return args

    assert counter == 0
    func(1)
    assert counter == 1
    func(1)
    assert counter == 1
    func(2)
    assert counter == 2
