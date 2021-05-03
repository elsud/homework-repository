"""
Given a list of integers numbers "nums".

You need to find a sub-array with length less equal to "k", with maximal sum.

The written function should return the sum of this sub-array.

Examples:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    result = 16
"""
from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int or None:
    """This function return sum of sub-array with length less equal to "k",
    with maximum sum. If list hasn't numbers then return None"""
    if not nums:
        return None

    max_sum = float("-inf")
    for sub_arr_len in range(1, k + 1):
        for start_pos in range(len(nums) - sub_arr_len + 1):
            new_sum = sum(nums[start_pos : start_pos + sub_arr_len])
            if new_sum > max_sum:
                max_sum = new_sum
    return max_sum
