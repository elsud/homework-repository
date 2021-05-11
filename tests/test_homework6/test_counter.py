import pytest

from homework6.counter import instances_counter


@pytest.fixture
def decorated():
    class Some:
        pass

    return instances_counter(Some)


def test_counter_is_zero_before_creating_instances(decorated):
    decorated.get_created_instances() == 0


def test_counter_match_count_of_created_instances(decorated):
    instance, _, _ = decorated(), decorated(), decorated()
    assert instance.get_created_instances() == 3


def test_counter_resets_with_reset_instances_counter(decorated):
    instance, _, _ = decorated(), decorated(), decorated()
    assert instance.reset_instances_counter() == 3
    assert decorated.get_created_instances() == 0
