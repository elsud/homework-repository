# -*- coding: utf-8 -*-
"""Test homework1/task02.py
"""


import sys

from homework1.task02 import check_fib


def test_positive_special_cases():
    """Testing that actual fib sequence with the special values return True"""
    assert check_fib([0])
    assert check_fib([1])
    assert check_fib([0, 1])
    assert check_fib([1, 1])


def test_positive_case_1_member():
    """Testing that actual fib sequence with 1 member return True"""
    assert check_fib([21])


def test_positive_case_2_members():
    """Testing that actual fib sequence with 2 member return True"""
    assert check_fib([21, 34])


def test_positive_case_many_members():
    """Testing that actual fib sequence with many member return True"""
    assert check_fib([34, 55, 89, 144, 233])


def test_negative_case_positive_seq():
    """Testing that not fib seq with positive values return False"""
    assert not check_fib([34, 54, 89])
    assert not check_fib([1, 1, 1, 1])
    assert not check_fib([0, 1, 1, 1])
    assert not check_fib((1, 1, 1, 1, sys.maxsize))


def test_negative_case_negative_seq():
    """Testing that not fib seq with negative and positive values give False"""
    assert not check_fib([34, 54, -89])
    assert not check_fib([-1, 0, 1])
    assert not check_fib([0, 0])
