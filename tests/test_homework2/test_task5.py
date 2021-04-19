import string

from homework2.task5 import custom_range


def test_custom_range_with_stop():
    """Testing that with iterable and one else arg that arg works as stop."""
    expected = ["a", "b", "c", "d", "e", "f"]
    assert custom_range(string.ascii_lowercase, "g") == expected


def test_custom_range_with_start_and_stop():
    """Testing that 2 args with iterable gives start and stop element for range."""
    expected = ["g", "h", "i", "j", "k", "l", "m", "n", "o"]
    assert custom_range(string.ascii_lowercase, "g", "p") == expected


def test_custom_range_with_step():
    """Testing that third arg after iterable works like a step for range."""
    expected = ["p", "n", "l", "j", "h"]
    assert custom_range(string.ascii_lowercase, "p", "g", -2) == expected
