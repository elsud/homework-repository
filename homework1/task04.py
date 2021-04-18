"""
Classic task, a kind of walnut for you

Given four lists A, B, C, D of integer values,
    compute how many tuples (i, j, k, l) there are such that
    A[i] + B[j] + C[k] + D[l] is zero.

We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.
"""
from typing import List
from itertools import product


def check_sum_of_four(
        list_a: List[int], list_b: List[int], list_c: List[int],
        list_d: List[int]
) -> int:
    """This function count number of tuples (i, j, k, l) there are such that
    a[i] + b[j] + c[k] + d[l] equal zero
    A, B, C, D must have same length of N where 0 ≤ N ≤ 1000"""
    count_tuples = 0
    sums = {}
    for a_val, b_val in product(list_a, list_b):
        if a_val + b_val not in sums:
            sums[a_val + b_val] = 1
        else:
            sums[a_val + b_val] += 1
    for c_val, d_val in product(list_c, list_d):
        if -(c_val + d_val) in sums:
            count_tuples += sums[-(c_val + d_val)]
    return count_tuples
