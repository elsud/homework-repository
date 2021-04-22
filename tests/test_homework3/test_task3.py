from homework3.task3 import make_filter, sample_data


def test_case_with_confliciting_filters():
    assert make_filter(name="polly", type="person").apply(sample_data) == []


def test_case_without_filter():
    assert make_filter().apply(sample_data) == sample_data
