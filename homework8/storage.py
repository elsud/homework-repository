from typing import Any


class KeyValueStorage:
    """It is a wrapper class for key-value storage readen from a file,
    where each line is represented as key and value separated with = symbol.
    If value is a number it's treated like a number, otherwise like a string.
    Keys and values become accessible as collection items and as attributes.
    If key cannot be assigned to an attribute(for example when it's a number)
    it raises ValueError.

    :param path: Path to the file with key_value storage
    :type path: str
    :raises ValueError: Raises when key cannnot be assigned to an attribute
    """

    def __init__(self, path=str):
        with open(path) as fi:
            for line in fi.readlines():
                name, value = line.strip().split("=")
                if not (name[0].isalpha() or name[0] == "_"):
                    raise ValueError
                value = int(value) if value.isdigit() else value
                self.__dict__[name] = value

    def __getitem__(self, name: str) -> Any:
        """Implements access to a value as a collection item.
        :param name: A key by which a corresponding value can be accessible
        :type name: str
        :return: value or None if there isn't such key
        "rtype: str or int or None
        """
        return self.__dict__.get(name, None)
