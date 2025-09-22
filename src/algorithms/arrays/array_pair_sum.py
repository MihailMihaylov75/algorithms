"""
Problem:
Given an array of integers and a target sum, find the number of unique pairs
of integers in the array that add up to the target sum.

Example:
    array_pair_sum([1, 3, 2, 2], 4) -> 2
    # (1, 3) and (2, 2)

Constraints:
- Input array may contain positive or negative integers.
- Pairs are unordered: (a, b) is considered the same as (b, a).
- Each unique pair is counted only once.
"""



def array_pair_sum(numbers: list[int], target: int) -> int:
    """
    Counts the number of unique pairs in the given list of integers that add up
    to the target sum.

    :param numbers: List of integers (may include duplicates).
    :param target: The target sum for the pairs.
    :return: The number of unique pairs that sum to the target.

    Time Complexity: O(n), where n = len(numbers).
    Space Complexity: O(n), due to auxiliary sets.
    """
    if not numbers:
        return 0

    seen = set()
    output = set()

    for num in numbers:
        complement = target - num
        if complement in seen:
            output.add(tuple(sorted((num, complement))))
        seen.add(num)

    return len(output)
