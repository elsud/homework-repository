import os
from pathlib import Path
from typing import Callable, Optional


def universal_file_counter(
    dir_path: Path, file_extension: str, tokenizer: Optional[Callable] = None
) -> int:
    """Takes directory path, a file extension and an optional tokenizer.
    Counts lines in all files with that extension if there are no tokenizer.
    Counts tokens if tokenizer is not None.
    :param dir_path: directory path where function will look for files
    :type dir_path: Path
    :param file_extension: file extension files with which will be opened
    with function
    :type file_extension: str
    :param tokenizer: tokenizer for files with right extension
    :type tokenizer: Callable or None
    :return: count of tokens if there are tokenizer or of the lines in files
    :rtype: int
    """
    count = 0
    flag = bool(tokenizer)
    all_files = os.listdir(dir_path)
    to_open = (file for file in all_files if file.endswith(file_extension))
    for file in to_open:
        with open(os.path.join(dir_path, file)) as fi:
            if flag:
                count += len(tokenizer(fi.read()))
            else:
                count += sum(1 for _ in fi)
    return count
