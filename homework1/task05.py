"""
Given a list of integers numbers "nums".

You need to find a sub-array with length less equal to "k", with maximal sum.

The written function should return the sum of this sub-array.

Examples:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    result = 16
"""
from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    """Finding maximal sum of sub-array with length less equal to given number."""
    i, j = 0, k
    total = sum(nums[:j])
    max_total = total
    while j < len(nums):
        total = total - nums[i] + nums[j]
        i += 1
        j += 1
        max_total = total if total > max_total else max_total
    return max_total
