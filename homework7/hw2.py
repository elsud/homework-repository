"""
Given two strings. Return if they are equal when both are typed into
empty text editors. # means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Examples:
    Input: s = "ab#c", t = "ad#c"
    Output: True
    # Both s and t become "ac".

    Input: s = "a##c", t = "#a#c"
    Output: True
    Explanation: Both s and t become "c".

    Input: a = "a#c", t = "b"
    Output: False
    Explanation: s becomes "c" while t becomes "b".

"""


def _sharp_is_backspace(strng):
    """Convert sharps (#) into backspaces"""
    str_arr = []
    for symbol in strng:
        if symbol == "#":
            try:
                str_arr.pop()
            except IndexError:
                pass
        else:
            str_arr.append(symbol)
    return "".join(str_arr)


def backspace_compare(first: str, second: str):
    """Compare two strings with # (= backspaces)"""
    return _sharp_is_backspace(first) == _sharp_is_backspace(second)
