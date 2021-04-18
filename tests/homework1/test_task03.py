# -*- coding: utf-8 -*-
"""Test homework1/task03.py
"""

import os.path

from homework1.task03 import find_max_and_min

PATH = os.path.join(os.path.dirname(__file__), "test_task_3_cases")


def test_2_num_cases():
    """Testing that actual file has 2 integers, positive cases"""
    assert find_max_and_min(os.path.join(PATH, "case1.txt")) == (
        1,
        1,
    ), "case1 fail"
    assert find_max_and_min(os.path.join(PATH, "case2.txt")) == (
        -100,
        100,
    ), "case2 fail"


def test_many_num_cases():
    """Testing that actual file has more then 2 integers, positive cases"""
    assert find_max_and_min(os.path.join(PATH, "case3.txt")) == (
        0,
        0,
    ), "case3 fail"
    assert find_max_and_min(os.path.join(PATH, "case4.txt")) == (
        -10,
        10,
    ), "case4 fail"


def test_empty_file():
    """Testing that actual file has 2 integers, positive cases"""
    assert find_max_and_min(os.path.join(PATH, "case5.txt")) == (
        None,
        None,
    ), "case5 fail"
