from homework7.backspace import backspace_compare


def test_backspacing_one_different_letter_gives_true():
    assert backspace_compare("ab#c", "ad#c")


def test_backspacing_all_besides_last_equal_letter_gives_true():
    assert backspace_compare("a##c", "##a#c")


def test_empty_strings_gives_true():
    assert backspace_compare("", "##")


def test_different_strings_gives_false():
    assert not backspace_compare("d", "d#f")
