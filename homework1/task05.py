"""
Given a list of integers numbers "nums".

You need to find a sub-array with length less equal to "k", with maximal sum.

The written function should return the sum of this sub-array.

Examples:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    result = 16
"""
from itertools import chain, islice
from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int or None:
    """This function return sum of sub-array with length less equal to "k",
    with maximum sum. If list hasn't numbers then return None"""
    if not nums:
        return None

    max_sum = float("-inf")
    for sub_arr_len in range(1, k + 1):
        # because black ruin max string len
        slices = chain(
            zip(range(0, len(nums) - sub_arr_len), range(sub_arr_len, len(nums))),
            ((len(nums) - sub_arr_len, None),),
        )
        for start_slice, end_slice in slices:
            sub_arr = islice(nums, start_slice, end_slice)
            new_sum = sum(sub_arr)
            if new_sum > max_sum:
                max_sum = new_sum
    return max_sum
