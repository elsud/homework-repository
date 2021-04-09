# -*- coding: utf-8 -*-
"""Calc
This module have only one function. It checks that number is
power of 2
"""


def check_power_of_2(number: int) -> bool:
    """
    Check that "a" is power of 2
    :param number: integer, checked number
    :return: True if power of 2 else False
    """
    return not bool(number & (number - 1))
