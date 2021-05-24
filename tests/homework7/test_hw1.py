"""Test homework7.hw1"""

from homework7.hw1 import find_occurrences

test_tree = {
    "first": ["RED", "BLUE"],
    "second": {
        "simple_key": ["simple", "list", "of", "RED", "valued"],
    },
    "third": {
        "abc": "BLUE",
        "jhl": "RED",
        "complex_key": {
            "key1": "value1",
            "key2": "RED",
            "key3": ["a", "lot", "of", "values", {"nested_key": "RED"}],
        }
    },
    "fourth": "RED",
}


def test_positive():
    """Test find_occurrences if dict has element"""
    assert find_occurrences(test_tree, "RED") == 6


def test_negative():
    """Test find_occurrences if dict hasn't element"""
    assert find_occurrences(test_tree, "PURPLE") == 0
