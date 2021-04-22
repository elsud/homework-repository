"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
from typing import List


def reading_text(file_path: str) -> List[str]:
    """Reading text from file in lines."""
    with open(file_path) as data:
        text = (line.encode().decode("unicode_escape") for line in data.readlines())
    return text


def get_longest_diverse_words(file_path: str) -> List[str]:
    """Search ten words with longest set of unique chars."""
    text = reading_text(file_path)
    punctuation = (".", ":", ",", "?", "!")
    longest_words = []
    for line in text:
        line = line.strip().split()
        for word in line:
            while word.endswith(punctuation):
                word = word[:-1]
            length = len(set(word))
            if (word, length) in longest_words:
                continue
            if len(longest_words) == 10:
                if length < longest_words[-1][1]:
                    continue
                if length == longest_words[-1][1]:
                    if len(word) > len(longest_words[-1][0]):
                        longest_words[-1] = (word, length)
                else:
                    longest_words[-1] = (word, length)
            else:
                longest_words.append((word, length))
            longest_words.sort(key=lambda x: -x[1])
    return [word for word, length in longest_words]


def get_rarest_char(file_path: str) -> str:
    """Counting frequency of every char in text and search the rarest one."""
    frequency = {}
    text = reading_text(file_path)
    for line in text:
        for char in line:
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1
    counter, rarest = float("inf"), None
    for k, v in frequency.items():
        if v < counter:
            rarest = k
            counter = v
    return rarest


def count_punctuation_chars(file_path: str) -> int:
    """Counting all punctuations chars in text."""
    punctuations = [",", ".", ":", ";", "?", "!", "(", ")", "—"]
    acc = 0
    text = reading_text(file_path)
    for line in text:
        for char in line:
            if char in punctuations:
                acc += 1
    return acc


def count_non_ascii_chars(file_path: str) -> int:
    """Counting all non ascii chars in text."""
    with open(file_path) as data:
        text = data.read()

    return text.count("\\")


def get_most_common_non_ascii_char(file_path: str) -> str:
    """Counting frequenty of every non ascii char and search most common."""
    frequency = {}
    text = reading_text(file_path)
    for line in text:
        for char in line:
            if not char.isascii():
                if char in frequency:
                    frequency[char] += 1
                else:
                    frequency[char] = 1
    counter, common = float("-inf"), None
    for k, v in frequency.items():
        if v > counter:
            common = k
    return common
