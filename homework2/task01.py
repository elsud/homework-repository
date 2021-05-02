"""Task01 - Text work"""
import string
from collections import namedtuple
from typing import List
from unicodedata import category

Token = namedtuple("Token", ["type", "value"])


def tokenize(file_path):
    """Tokenizing"""
    buffer = ""
    symbol = file_path.read(1)
    while symbol:
        if category(symbol).startswith("L"):
            buffer += symbol
            symbol = file_path.read(1)
            continue
        if symbol == "-":
            symbol = file_path.read(1)
            if symbol == "\n":
                symbol = file_path.read(1)
                buffer += symbol
                symbol = file_path.read(1)
            continue
        if buffer:
            yield Token("word", buffer)
            buffer = ""
        yield Token("symbol", symbol)
        symbol = file_path.read(1)
    yield Token("word", buffer)


def get_longest_diverse_words(file_name: str) -> List[str]:
    """10 unique longest words"""

    def remove_duplicate(word):
        """Delete same symbols"""
        if (len(word)) < 2:
            return word
        result = []
        for i in word:
            if i not in result:
                result.append(i)
        return "".join(result)

    def sort_by_length(input_str):
        """Key for func sorted"""
        return len(input_str)

    words = {}

    with open(file_name, mode="r", encoding="unicode-escape", errors="ignore") as file:
        for token in tokenize(file):
            if token.type == "word":
                unique_symbols = remove_duplicate(token.value)
                words[unique_symbols] = token.value
        sorted_words = sorted(words.values(), key=sort_by_length)
        ten_unique_words = sorted_words[-11:-1]
    return ten_unique_words


def get_rarest_char(file_name: str) -> str:
    """Rarest symbol"""
    sums = {}
    with open(file_name, mode="r", encoding="unicode-escape", errors="ignore") as fi:
        for symbol in fi.read():
            if symbol not in sums:
                sums[symbol] = 1
            else:
                sums[symbol] += 1
        rarest_symbols = ""
        for symbol, num in sums.items():
            if num == 1:
                rarest_symbols += symbol
        return rarest_symbols


def count_punctuation_chars(file_name: str) -> int:
    """Count punctuation"""
    counter_punctuation = 0
    with open(file_name, mode="r", encoding="unicode-escape", errors="ignore") as fi:
        for punctuation in fi.read():
            if punctuation in string.punctuation:
                counter_punctuation += 1
        return counter_punctuation


def count_non_ascii_chars(file_name: str) -> int:
    """Count non ascii char"""
    counter_non_ascii = 0
    with open(file_name, mode="r", encoding="unicode-escape", errors="ignore") as fi:
        for symbol in fi.read():
            if ord(symbol) > 127:
                counter_non_ascii += 1
        return counter_non_ascii


def get_most_common_non_ascii_char(file_name: str) -> str:
    """Most common non ascii char"""
    sums = {}
    largest_num = 0
    largest_symbol = ""
    with open(file_name, mode="r", encoding="unicode-escape", errors="ignore") as fi:
        for symbol in fi.read():
            if ord(symbol) > 127:
                if symbol not in sums:
                    sums[symbol] = 1
                else:
                    sums[symbol] += 1
        for symbol, num in sums.items():
            if num > largest_num:
                largest_symbol = symbol
                largest_num = num
        return largest_symbol
