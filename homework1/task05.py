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
    """This function return sum of sub-array with length less equal to "k",
    with maximum sum. Nums must have one number at least"""
    assert len(nums) > 0
    nums_positive_only = [element for element in nums if element > 0]
    if len(nums_positive_only) == 0:
        return max(nums)
    if len(nums_positive_only) < k:
        return sum(nums_positive_only)
    nums_positive_only.sort()
    return sum(nums_positive_only[-k:])
