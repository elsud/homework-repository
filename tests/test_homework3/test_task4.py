from homework3.task4 import is_armstrong, is_armstrong_string_solution


def test_if_armstrong_is_armstrong():
    assert is_armstrong(153)
    assert is_armstrong(1)


def test_if_non_armstrong_is_not_armstrong():
    assert not is_armstrong(10)


def test_if_armstrong_is_armstrong_in_string_solution():
    assert is_armstrong_string_solution(153)


def test_if_non_armstrong_is_not_armstrong_in_string_solution():
    assert not is_armstrong_string_solution(13)
