def _sharp_is_backspace(strng):
    str_arr = []
    for symbol in strng:
        str_arr.pop() if symbol == '#' else str_arr.append(symbol)
    return ''.join(str_arr)


def backspace_compare(first: str, second: str):
    return _sharp_is_backspace(first) == _sharp_is_backspace(second)