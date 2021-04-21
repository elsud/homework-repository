# -*- coding: utf-8 -*-
"""Test homework1/task03.py
"""

import os.path

from homework1.task03 import find_max_and_min

PATH = os.path.join(os.path.dirname(__file__), "test_task_3_cases")


def test_test_find_max_and_min_empty_file():
    assert find_max_and_min(os.path.join(PATH, "empty.txt")) == (None, None)


def test_test_find_max_and_min_1_value():
    assert find_max_and_min(os.path.join(PATH, "1_value.txt")) == (1, 1)


def test_test_find_max_and_min_2_same_values():
    assert find_max_and_min(os.path.join(PATH, "2_same_values.txt")) == (
        1,
        1,
    )


def test_test_find_max_and_min_2_different_values():
    assert find_max_and_min(os.path.join(PATH, "2_different_values.txt")) == (
        -100,
        100,
    )


def test_test_find_max_and_min_many_same_values():
    assert find_max_and_min(os.path.join(PATH, "many_same_values.txt")) == (0, 0)


def test_test_find_max_and_min_many_different_values():
    assert find_max_and_min(os.path.join(PATH, "many_different_values.txt")) == (
        -10,
        10,
    )
