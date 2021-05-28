import heapq
from pathlib import Path
from typing import Generator, Iterator, List, Union


def iter_from_file(file: Union[Path, str]) -> Generator[int, None, None]:
    """Reads file with sorted integers and yield that integers by one.
    :param file: path to file with integers
    :type file: str or path
    :return: generator which yield integers from the file
    :rtype: Generator
    """
    with open(file) as fi:
        for line in fi.readlines():
            yield int(line.strip())


def merge_sorted_files(file_list: List[Union[Path, str]]) -> Iterator:
    """Takes list of pathes to files which consists of sorted integers,
    merges that integers in sort and returns an iterator with them.
    :param file_list: list whith pathes to files
    :type file_list: list
    :return: iterator through sorted integers from files
    :rtype: Iterator
    """
    return heapq.merge(*(iter_from_file(file) for file in file_list))
