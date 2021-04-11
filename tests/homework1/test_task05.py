# -*- coding: utf-8 -*-
"""Test homework1/task05.py
"""

from homework1.task05 import find_maximal_subarray_sum


def test_negative_nums_only():
    """Test with length of list equal to 0"""
    assert find_maximal_subarray_sum([-1, -2, -5, -50], 3) == -1


def test_positive_nums_less_than_k():
    """Test with length of list equal to 0"""
    assert find_maximal_subarray_sum([1, 2, -5, -50], 3) == 3


def test_positive_nums_more_than_k():
    """Test with length of list equal to 0"""
    assert find_maximal_subarray_sum([1, 2, 5, 50], 3) == 57
