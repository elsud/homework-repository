# -*- coding: utf-8 -*-
"""Test homework1/task04.py
"""

from random import randint
from time import time

from homework1.task04 import check_sum_of_four


def test_correctness_with_no_values():
    """Test with length of list equal to 0"""
    assert check_sum_of_four([], [], [], []) == 0


def test_correctness_with_1_value():
    """Test with length of list equal to 1"""
    assert check_sum_of_four([1], [2], [3], [4]) == 0
    assert check_sum_of_four([-1], [-20], [1], [20]) == 1


def test_correctness_with_many_values():
    """Test with length of list more than 1"""
    assert check_sum_of_four([-1, 1], [-2, 2], [2, -2], [1, -1]) == 4
    assert check_sum_of_four([0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]) == 81


def test_time_to_solve():
    """Test that the time to solve the problem is not very long"""
    a = [randint(-5 * 10 ** 9, 5 * 10 ** 9) for _ in range(200)]
    b = [randint(-5 * 10 ** 9, 5 * 10 ** 9) for _ in range(200)]
    c = [randint(-5 * 10 ** 9, 5 * 10 ** 9) for _ in range(200)]
    d = [randint(-5 * 10 ** 9, 5 * 10 ** 9) for _ in range(200)]
    start_time = time()
    check_sum_of_four(a, b, c, d)
    time_to_solve_with_1000_members = (time() - start_time) * 5 ** 4
    assert time_to_solve_with_1000_members < 1800
