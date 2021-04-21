# -*- coding: utf-8 -*-
"""Test homework1/task02.py
"""

import sys

import pytest

from homework1.task02 import check_fib


@pytest.mark.parametrize("one_elem_seq", [[0], [1], [21]])
def test_check_fib_positive_one_elem_cases(one_elem_seq):
    assert check_fib(one_elem_seq)


@pytest.mark.parametrize("one_elem_seq", [[-100], [-1], [4]])
def test_check_fib_negative_one_elem_cases(one_elem_seq):
    assert not check_fib(one_elem_seq)


@pytest.mark.parametrize("two_elem_seq", [[0, 1], [1, 1], [13, 21]])
def test_check_fib_positive_two_elem_cases(two_elem_seq):
    assert check_fib(two_elem_seq)


@pytest.mark.parametrize(
    "two_elem_seq",
    [
        [-1, -1],
        [0, 0],
        [1, 3],
        [14, 21],
        [13, 22],
    ],
)
def test_check_fib_negative_two_elem_cases(two_elem_seq):
    assert not check_fib(two_elem_seq)


@pytest.mark.parametrize("many_elem_seq", [[0, 1, 1, 2], [2, 3, 5, 8, 13]])
def test_check_fib_positive_many_elem_cases(many_elem_seq):
    assert check_fib(many_elem_seq)


@pytest.mark.parametrize(
    "many_elem_seq",
    [
        [0, 1, 1, 3],
        [1, 1, 1, 2],
        [2, 3, 5, 9, 13],
        [-1, 0, 1, 2],
        [1, 1, 1, 1, sys.maxsize],
    ],
)
def test_check_fib_negative_many_elem_cases(many_elem_seq):
    assert not check_fib(many_elem_seq)
