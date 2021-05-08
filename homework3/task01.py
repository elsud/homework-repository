"""Test for task03 - Cache n times"""


def make_key(args, kwargs):
    return args, frozenset(sorted(kwargs.items()))


def cache(times=2):
    def wrapper(func):
        cached_value = {}

        def inner(*args, **kwargs):
            key = make_key(args, kwargs)
            if key not in cached_value:
                res = func(*args, **kwargs)
                cached_value[key] = [res, 0]
            res, called = cached_value[key]
            if called > times:
                return func(*args, **kwargs)
            else:
                cached_value[key][1] += 1
                return res

        return inner

    return wrapper
