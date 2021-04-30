"""Testing sum of slow_calculate doesn't take more than a minute."""
import time
from functools import wraps

from homework3.task2 import slow_calculate, sum_of_slow_calculate


def timer(func):
    """Timing how long does it take to execute function."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        duration = time.time() - start
        return duration

    return wrapper


def test_if_speed_of_sum_calculate_is_less_than_minute():
    assert timer(sum_of_slow_calculate)(500) <= 60


def test_if_sum_calculate_is_sum_of_slow_calculate():
    expected = slow_calculate(0) + slow_calculate(1)
    assert sum_of_slow_calculate(2) == expected
