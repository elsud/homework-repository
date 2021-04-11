# -*- coding: utf-8 -*-
"""Calc
This module have only one function. It checks that number is
power of 2
"""


def check_power_of_2(number: int) -> bool:
    """Check that "a" is power of 2
    """
    return not bool(number & (number - 1))
