# -*- coding: utf-8 -*-
"""Test homework1/task03.py
"""

import os.path
import random
import string

import pytest

from homework1.task03 import find_max_and_min


@pytest.fixture()
def make_file(tmp_path):
    def file_factory(body_text):
        while True:
            file_name = "".join(random.choices(string.ascii_lowercase, k=10))
            file_path = os.path.join(tmp_path, file_name)
            if not os.path.exists(file_path):
                break

        with open(file_path, "w") as fout:
            fout.write(body_text)
        return file_path

    return file_factory


def test_test_find_max_and_min_empty_file(make_file):
    file = make_file("")
    assert find_max_and_min(file) == (None, None)


def test_test_find_max_and_min_1_value(make_file):
    file = make_file("1")
    assert find_max_and_min(file) == (1, 1)


def test_test_find_max_and_min_2_same_values(make_file):
    file = make_file("1  \n 1")
    assert find_max_and_min(file) == (1, 1)


def test_test_find_max_and_min_2_different_values(make_file):
    file = make_file("-100\n100")
    assert find_max_and_min(file) == (-100, 100)


def test_test_find_max_and_min_many_same_values(make_file):
    file = make_file("0\n0\n0\n0\n0\n")
    assert find_max_and_min(file) == (0, 0)


def test_test_find_max_and_min_many_different_values(make_file):
    file = make_file("-5\n-10\n10\n1\n2")
    assert find_max_and_min(file) == (-10, 10)
