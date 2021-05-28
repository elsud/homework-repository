import pytest

from homework8.storage import KeyValueStorage

TEXT = "name=kek\nlast_name=top\npower=9001\nsong=shadilay\n__class__=123"
ERROR = "1=some"


def test_if_value_raises_when_key_cannot_be_assigned_to_an_attribute(tmp_path):
    path_to_error = tmp_path / "error.txt"
    with open(path_to_error, "w") as fi:
        fi.write(ERROR)
    with pytest.raises(ValueError):
        KeyValueStorage(path_to_error)


def test_value_accessible_by_atribute(tmp_path):
    path = tmp_path / "text.txt"
    with open(path, "w") as fi:
        fi.write(TEXT)
    storage = KeyValueStorage(path)
    assert storage.song == "shadilay"


def test_value_accessible_as_collection_item(tmp_path):
    path = tmp_path / "text.txt"
    with open(path, "w") as fi:
        fi.write(TEXT)
    storage = KeyValueStorage(path)
    assert storage["last_name"] == "top"


def test_value_is_integer_when_it_is_a_number(tmp_path):
    path = tmp_path / "text.txt"
    with open(path, "w") as fi:
        fi.write(TEXT)
    storage = KeyValueStorage(path)
    assert isinstance(storage.power, int)


def test_precedence_of_built_in_atributes(tmp_path):
    path = tmp_path / "text.txt"
    with open(path, "w") as fi:
        fi.write(TEXT)
    storage = KeyValueStorage(path)
    assert storage["__class__"] == 123
    assert not storage["__class__"] == storage.__class__
    assert isinstance(storage.__class__, type)
