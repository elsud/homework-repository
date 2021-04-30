import pytest

from homework4.task1 import read_magic_number


def test_not_existing_file_raises_error(tmp_path):
    path_to_nowhere = tmp_path / "not_existing.txt"
    with pytest.raises(ValueError):
        read_magic_number(path_to_nowhere)


def test_empty_file_gives_false(tmp_path):
    path_to_empty = tmp_path / "empty.txt"
    with open(path_to_empty, "w"):
        pass
    assert not read_magic_number(path_to_empty)


def test_file_with_text_gives_false(tmp_path):
    path_to_text = tmp_path / "text.txt"
    with open(path_to_text, "w") as text:
        text.write("some text inside")
    assert not read_magic_number(path_to_text)


def test_file_with_1_gives_true(tmp_path):
    path_to_number = tmp_path / "number.txt"
    with open(path_to_number, "w") as one:
        one.write("1\n")
    assert read_magic_number(path_to_number)


def test_file_with_3_gives_false(tmp_path):
    path_to_number = tmp_path / "number.txt"
    with open(path_to_number, "w") as three:
        three.write("3\n")
    assert not read_magic_number(path_to_number)


def test_file_with_almost_3_gives_true(tmp_path):
    path_to_number = tmp_path / "number.txt"
    with open(path_to_number, "w") as suitable:
        suitable.write("2.9999")
    assert read_magic_number(path_to_number)


def test_file_with_number_less_than_one_gives_false(tmp_path):
    path_to_number = tmp_path / "number.txt"
    with open(path_to_number, "w") as nonsuitable:
        nonsuitable.write("0.9999")
    assert not read_magic_number(path_to_number)
