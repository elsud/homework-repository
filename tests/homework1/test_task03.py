# -*- coding: utf-8 -*-
"""Test homework1/task03.py
"""


from homework1.task03 import find_maximum_and_minimum

PATH = "tests/homework1/test_task_3_cases/"


def test_2_num_cases():
    """Testing that actual file has 2 integers, positive cases"""
    assert find_maximum_and_minimum(PATH + "case1.txt") == (1, 1), "case1 fail"
    assert find_maximum_and_minimum(PATH + "case2.txt") == (-100, 100), "case2 fail"


def test_many_num_cases():
    """Testing that actual file has more then 2 integers, positive cases"""
    assert find_maximum_and_minimum(PATH + "case3.txt") == (0, 0), "case3 fail"
    assert find_maximum_and_minimum(PATH + "case4.txt") == (-10, 10), "case4 fail"
