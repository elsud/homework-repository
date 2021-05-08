"""Test for task03 - Cache n times"""
from unittest.mock import Mock, call

from homework3.task01 import cache


def test_cache_with_same_arg():
    """Testing that program calls the same function only 2 times"""
    mock = Mock()
    cached_func = cache(times=1)(mock)
    cached_func(1, 3)
    cached_func(1, 3)
    cached_func(1, 3)
    assert mock.mock_calls == [call(1, 3), call(1, 3)]


def test_not_cache_with_different_arg():
    """Testing that program puts values from
    cache for each set of args only 1 time"""
    mock = Mock()
    cached_func = cache(times=1)(mock)
    cached_func(1, 3)
    cached_func(5, 2)
    cached_func(1, 3)
    cached_func(5, 2)
    cached_func(1, 3)
    cached_func(5, 2)
    assert mock.mock_calls == [call(1, 3), call(5, 2), call(1, 3), call(5, 2)]
