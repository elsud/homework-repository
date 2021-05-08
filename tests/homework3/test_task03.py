"""Test for task04 - Filter"""
from homework3.task03 import make_filter, sample_data


def test_case_run_throw_filter():
    assert make_filter(name="polly", type="bird").apply(sample_data) == [
        {"is_dead": True, "kind": "parrot", "name": "polly", "type": "bird"}
    ]


def test_case__conflict_with_filters():
    assert make_filter(name="polly", type="person").apply(sample_data) == []


def test_case_without_filter():
    assert make_filter().apply(sample_data) == sample_data
