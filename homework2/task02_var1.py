"""Task02_var1 - Most&least common"""
from collections import Counter
from typing import List, Tuple

nums = [int(i) for i in input().split()]


def major_and_minor_elem(inp: List) -> Tuple[int, int]:
    """Finds the most and least common elements in list"""
    sums = Counter(inp).most_common()
    if sums[-1][1] == sums[-2][1]:
        inp = [
            int(i)
            for i in input(
                "More than 1 element is the least common. Please, input right list "
            ).split()
        ]
        return major_and_minor_elem(inp)
    else:
        return sums[0][0], sums[-1][0]
