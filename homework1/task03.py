"""
Write down the function, which reads input line-by-line, and find maximum and
    minimum values.
Function should return a tuple with the max and min values.

For example for [1, 2, 3, 4, 5], function should return [1, 5]

We guarantee, that file exists and contains line-delimited integers.

To read file line-by-line you can use this snippet:

with open("some_file.txt") as fi:
    for line in fi:
        ...

"""
from typing import Tuple


def get_value_from_file(file_name):
    """Yield line's value from file"""
    with open(file_name) as fin:
        try:
            for line in fin:
                yield int(line.strip())
        except ValueError:
            return


def find_max_and_min(file_name: str) -> Tuple[int or None, int or None]:
    """This function take file path and return a tuple with max and
    min values. File must exists and contains line-delimited integers.

    :param file_name: a file path. File must exists and contains line-delimited
     integers.
    :return: tuple(min_value, max_value)
    """
    min_value, max_value = float("inf"), float("-inf")
    for line_value in get_value_from_file(file_name):
        if line_value > max_value:
            max_value = line_value
        if line_value < min_value:
            min_value = line_value
    return (min_value, max_value) if min_value < float("inf") else (None, None)
