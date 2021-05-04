"""Test for task02_var1 - Most&least common"""
from homework2.task02_var1 import major_and_minor_elem


def test_correct_input_for_counting(monkeypatch):
    """Testing right input"""
    num_input = [1, 1, 1, 2]
    monkeypatch.setattr("homework2.task02_var1.input_list", lambda: num_input)
    assert major_and_minor_elem(num_input) == (1, 2)


def test_2_less_common_elements(monkeypatch):
    """Testing wrong input"""
    num_input = [1, 1, 1, 2, 3]
    monkeypatch.setattr("homework2.task02_var1.input_list", lambda: num_input)
    num_input_right = [1, 1, 2]
    monkeypatch.setattr(
        "homework2.task02_var1.input_list_if_wrong", lambda: num_input_right
    )
    assert major_and_minor_elem(num_input) == (1, 2)
