# -*- coding: utf-8 -*-
"""Test homework1/task05.py
"""

from homework1.task05 import find_maximal_subarray_sum


def test_negative_nums_only():
    """Test with negative nums only"""
    assert find_maximal_subarray_sum([-1, -2, -5, -50], 3) == -1


def test_positive_and_negatives_nums():
    """Test with positive and negatives nums"""
    assert find_maximal_subarray_sum([1, 2, -5, -50], 3) == 3


def test_positive_nums_only():
    """Test with positive nums only"""
    assert find_maximal_subarray_sum([1, 2, 5, 50], 3) == 57
    assert find_maximal_subarray_sum([1, 2, 1, 2, 1], 2) == 3
    assert find_maximal_subarray_sum([1, 2, 1, 2, 1, 3], 2) == 4
