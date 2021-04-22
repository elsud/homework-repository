"""Testing cache function caches results for n invokes."""

from homework3.task1 import cache


def test_if_result_is_cached():
    func = cache()(sum)
    first = func(range(300, 305))
    second = func(range(300, 305))
    assert first is second


def test_test_if_result_cached_only_n_times():
    func = cache(1)(sum)
    first, *_, third = (func(range(300, 305)) for _ in range(3))
    assert first is not third
