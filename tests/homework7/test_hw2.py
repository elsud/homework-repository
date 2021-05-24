"""Test homework7.hw2"""

from homework7.hw2 import backspace_compare


def test_without_hash_negative():
    """Test backspace_compare if strings haven't hash. Negative"""
    assert not backspace_compare('123abcЙЦУКЕН', '123abcQWERTY')


def test_without_hash_positive():
    """Test backspace_compare if strings haven't hash. Positive"""
    assert backspace_compare('123abcЙЦУКЕН', '123abcЙЦУКЕН')


def test_backspace_compare_general():
    """Test backspace_compare. Positive"""
    assert backspace_compare('123#abc##ЙЦУКЕН###', '12aЙЦУ')
