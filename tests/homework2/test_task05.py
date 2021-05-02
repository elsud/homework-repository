"""Tests for task05 - Custom range"""
from string import ascii_lowercase

from homework2.task05 import custom_range


def test_custom_range_different_range():
    """Testing how func slices"""
    assert custom_range(ascii_lowercase) == [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
    ]
    assert custom_range(ascii_lowercase, "g") == ["a", "b", "c", "d", "e", "f"]
    assert custom_range(ascii_lowercase, "g", "p") == [
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
    ]
    assert custom_range(ascii_lowercase, "p", "g", -2) == ["p", "n", "l", "j", "h"]
