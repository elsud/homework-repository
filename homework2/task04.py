"""Task04 - Cache"""
from typing import Callable


def cache(func: Callable) -> Callable:
    """Caches call to another function"""
    cached_value = {}

    def wrapped(*args):
        key = args
        if key in cached_value:
            return cached_value[key]
        else:
            res = func(*args)
            cached_value[key] = res
            return res

    return wrapped
