"""Task02_var2 - Most&least common"""
from collections import Counter
from typing import List, Tuple

nums = [int(i) for i in input().split()]


def major_and_minor_elem(inp: List) -> Tuple[int, int]:
    """Finds the most and least common elements in list"""
    sums = Counter(inp).most_common()
    n = len(inp)
    if sums[0][1] <= n // 2:
        inp = [
            int(i)
            for i in input(
                "There is not element, which fills list more than n//2. Please, input right list "
            ).split()
        ]
        return major_and_minor_elem(inp)
    elif sums[-1][1] == sums[-2][1]:
        inp = [
            int(i)
            for i in input(
                "More than 1 element is the least common. Please, input right list "
            ).split()
        ]
        return major_and_minor_elem(inp)
    else:
        return sums[0][0], sums[-1][0]
