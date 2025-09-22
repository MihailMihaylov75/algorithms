"""
Problem:
Given an integer array (may include negatives), return the maximum sum over all
non-empty contiguous subarrays. If the input is empty, return 0.

Examples:
    largest_contiguous_sum([1, -2, 3, 4, -1, 2, -5, 4]) -> 8    # 3+4-1+2
    largest_contiguous_sum([-2, -3, -1, -5]) -> -1
    largest_contiguous_sum([]) -> 0

Notes:
- Implementation uses Kadane's algorithm.
- Time Complexity: O(n)
- Space Complexity: O(1)
"""

from collections.abc import Sequence


def largest_contiguous_sum(nums: Sequence[int]) -> int:
    """
    Returns the maximum sum of any contiguous subarray.
    For an empty input, returns 0.

    :param nums: Sequence of integers (can be empty; can contain negatives).
    :return: Maximum contiguous subarray sum (or 0 if empty).
    """
    if not nums:
        return 0

    max_sum = current = nums[0]
    for x in nums[1:]:
        current = max(x, current + x)
        max_sum = max(max_sum, current)
    return max_sum
