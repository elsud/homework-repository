"""Task02_var2 - Most&least common"""
from collections import Counter
from typing import List, Tuple


def input_list():
    nums = [int(i) for i in input().split()]
    return nums


def input_list_if_wrong():
    nums = [int(i) for i in input().split()]
    return nums


def major_and_minor_elem(inp: List) -> Tuple[int, int]:
    """Finds the most and least common elements in list"""
    sums = Counter(inp).most_common()
    n = len(inp)
    if sums[0][1] <= n // 2:
        print(
            "There is not element, which fills list more than n//2. Please, input right list!"
        )
        return major_and_minor_elem(input_list_if_wrong())
    elif sums[-1][1] == sums[-2][1]:
        print("More than 1 element is the least common. Please, input right list!")
        return major_and_minor_elem(input_list_if_wrong())
    else:
        return sums[0][0], sums[-1][0]
