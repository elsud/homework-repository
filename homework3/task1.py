"""Module with a parametrized cache decorator that remembers function
output value and gives out cached value up to n times only."""

from functools import wraps
from typing import Callable


def cache(times: int = 1) -> Callable:
    """Caching function output and giving out it up to given times.
    It's dict saves output value and quantity of times decorator should
    return this value instead of invoke function."""

    def decorator(func):
        func_cache_dict = {}

        @wraps(func)
        def wrapper(*args, **kwargs):
            key = args + tuple(sorted(kwargs.items()))
            if key in func_cache_dict:
                while func_cache_dict[key][1] > 0:
                    func_cache_dict[key][1] -= 1
                    return func_cache_dict[key][0]
            func_cache_dict[key] = [func(*args, **kwargs), times]
            return func_cache_dict[key][0]

        return wrapper

    return decorator
