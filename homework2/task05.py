"""Task05 - Custom range"""
from typing import List


def custom_range(source: str, *args) -> List[str]:
    """Making own custom range"""
    start_el = stop_el = step = None
    if len(args) == 1:
        start_el, stop_el, step = None, source.index(args[0]), None
    if len(args) == 2:
        start_el, stop_el, step = source.index(args[0]), source.index(args[1]), None
    if len(args) == 3:
        start_el, stop_el, step = source.index(args[0]), source.index(args[1]), args[2]
    return list(source[start_el:stop_el:step])
