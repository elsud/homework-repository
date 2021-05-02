"""Test for task02_var1 - Most&least common"""
from homework2.task02_var1 import major_and_minor_elem


def test_correct_input_for_counting():
    """Testing right input"""
    assert major_and_minor_elem([1, 1, 2]) == 1, 2
