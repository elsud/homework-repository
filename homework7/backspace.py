"""
Given two strings. Backspace_compare returns if they are equal
when both are typed into empty text editors. # means a backspace character.
"""
from itertools import zip_longest


def backspace_compare(first: str, second: str) -> bool:
    """Checking if strings are equal after printing if # means a backspace."""

    def custom_gen(word: str):
        """Yielding not backspaced letters from the end of the string."""
        backspace = 0
        for letter in reversed(word):
            if not backspace and letter != "#":
                yield letter
            elif letter == "#":
                backspace += 1
                continue
            else:
                backspace -= 1
                continue

    for letter1, letter2 in zip_longest(custom_gen(first), custom_gen(second)):
        if letter1 != letter2:
            return False

    return True
