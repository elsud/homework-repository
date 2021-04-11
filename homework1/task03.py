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


def find_maximum_and_minimum(file_name: str) -> Tuple[int, int]:
    """This function take file path and return a tuple with max and
    min values. File must exists and contains line-delimited integers.

    :param file_name: a file path. File must exists and contains line-delimited
     integers.
    :return: tuple(min_value, max_value)
    """
    with open(file_name) as fin:
        min_value = max_value = int(next(fin).strip())
        for line in fin:
            line_value = int(line.strip())
            if line_value > max_value:
                max_value = line_value
            elif line_value < min_value:
                min_value = line_value
    return min_value, max_value
