"""Test for task04 - Armstrong number"""
from homework3.task04 import is_armstrong


def test_if_armstrong_is_armstrong():
    assert is_armstrong(153), "Is Armstrong number"
    assert is_armstrong(1), "Is Armstrong number"


def test_if_non_armstrong_is_not_armstrong():
    assert not is_armstrong(10), "Is not Armstrong number"
