# -*- coding: utf-8 -*-
"""Test homework1/task05.py
"""

from homework1.task05 import find_maximal_subarray_sum


def test_find_maximal_subarray_sum_negative_nums_only():
    assert find_maximal_subarray_sum([-1, -2, -5, -50], 3) == -1


def test_find_maximal_subarray_sum_positive_and_negatives_nums():
    assert find_maximal_subarray_sum([2, -1, 2, -5, -50], 3) == 3


def test_find_maximal_subarray_sum_positive_nums_only_3_val():
    assert find_maximal_subarray_sum([1, 2, 5, 50], 3) == 57


def test_find_maximal_subarray_sum_positive_nums_only_2_val():
    assert find_maximal_subarray_sum([1, 2, 1, 2, 1], 2) == 3
