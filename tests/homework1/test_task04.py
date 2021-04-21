# -*- coding: utf-8 -*-
"""Test homework1/task04.py
"""

from random import randint
from time import time

import pytest

from homework1.task04 import check_sum_of_four


def test_check_sum_of_four_with_empty_lists():
    assert check_sum_of_four([], [], [], []) == 0


@pytest.mark.parametrize(
    "one_elem_seqs, expected",
    [
        (([1], [2], [3], [4]), 0),
        (([-1], [-20], [1], [20]), 1),
    ],
)
def test_check_sum_of_four_with_1_value_lists(one_elem_seqs, expected):
    assert check_sum_of_four(*one_elem_seqs) == expected


@pytest.mark.parametrize(
    "many_elem_seqs, expected",
    [
        (([-1, 1], [-2, 2], [2, -2], [1, -1]), 4),
        (([0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]), 81),
    ],
)
def test_check_sum_of_four_with_many_values(many_elem_seqs, expected):
    assert check_sum_of_four(*many_elem_seqs) == expected


def test_time_to_solve():
    """Test that the time to solve the problem is not very long"""
    list_a = [randint(-5 * 10 ** 9, 5 * 10 ** 9) for _ in range(200)]
    list_b = [randint(-5 * 10 ** 9, 5 * 10 ** 9) for _ in range(200)]
    list_c = [randint(-5 * 10 ** 9, 5 * 10 ** 9) for _ in range(200)]
    list_d = [randint(-5 * 10 ** 9, 5 * 10 ** 9) for _ in range(200)]

    start_time = time()
    check_sum_of_four(list_a, list_b, list_c, list_d)
    time_to_solve_with_1000_members = (time() - start_time) * 5 ** 4

    assert time_to_solve_with_1000_members < 1800
