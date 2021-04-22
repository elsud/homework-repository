from homework2.task4 import cache


def test_cache():
    """Testing that call to function was cached."""

    def func(arg1, arg2):
        return arg1 * arg2

    first = cache(func)(100, 200)
    second = cache(func)(100, 200)
    assert first is second
