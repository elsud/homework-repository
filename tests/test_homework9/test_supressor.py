import pytest

from homework9.supressor import Supressor, supressor


def test_class_supresses_passed_exception():
    with Supressor(IndexError):
        [][3]


def test_class_does_not_supress_another_exception():
    with pytest.raises(TypeError):
        with Supressor(IndexError):
            5[3]


def test_generator_supresses_passed_exception():
    with supressor(IndexError):
        [][3]


def test_generator_does_not_supress_another_exception():
    with pytest.raises(TypeError):
        with supressor(IndexError):
            4[5]
