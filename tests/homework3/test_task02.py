"""Test for task02 - Pool"""
from homework3.task02 import do


def test_right_sum():
    """Testing that program gives the right sum"""
    assert do() == 1025932
