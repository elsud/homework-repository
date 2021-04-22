from homework1.task02 import check_fibonacci


def test_empty_sequence():
    """Testing that empty sequence gives True."""
    assert check_fibonacci([])


def test_positive_case():
    """Testing that fibonacci sequences give True."""
    assert check_fibonacci([0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89])


def test_negative_case():
    """Testing that not fibonacci sequences give False."""
    assert not check_fibonacci([0, 1, 1, 2, 3, 5, 8, 13, 22])


def test_one_element_sequence():
    """Testing that sequences of 1 element give correct result."""
    assert not check_fibonacci("1")


def test_two_elements_sequence():
    """Testing that sequences of two elements give correct result."""
    assert check_fibonacci([0, 1])
