"""
Problem:
Given a target amount and coin denominations, return the minimum number of coins
to make the target. If impossible, raise ValueError.

Examples:
    min_coins_memo(63, [1,5,10,25]) -> 6
    min_coins_memo(0,  [1,5,10])    -> 0

Notes:
- Two versions: naive recursion and memoized DP.
- Time:
    * naive: exponential
    * memo: O(target * len(coins)) worst-case
- Space:
    * recursion depth up to target (naive), memo uses O(target)
"""

from collections.abc import Iterable, Sequence
from functools import cache


def min_coins_naive(target: int, coins: Sequence[int]) -> int:
    """
    Naive recursive solution (educational).

    :param target: Target amount (>= 0).
    :param coins: Available coin denominations (positives).
    :return: Minimum number of coins.
    :raises ValueError: If impossible to make exact change.
    """
    if target == 0:
        return 0
    if target < 0:
        raise ValueError("Impossible to make negative target")
    if not coins:
        raise ValueError("No coins provided")

    best = None
    for c in coins:
        if c <= target:
            try:
                candidate = 1 + min_coins_naive(target - c, coins)
                best = candidate if best is None or candidate < best else best
            except ValueError:
                # ignore impossible branch
                pass
    if best is None:
        raise ValueError("No combination makes the target")
    return best


def min_coins_memo(target: int, coins: Iterable[int]) -> int:
    """
    Memoized DP solution.

    :param target: Target amount (>= 0).
    :param coins: Iterable of coin denominations (positives).
    :return: Minimum number of coins.
    :raises ValueError: If impossible to make exact change.
    """
    denoms = tuple(sorted(set(c for c in coins if c > 0)))
    if target < 0:
        raise ValueError("target must be >= 0")
    if not denoms:
        if target == 0:
            return 0
        raise ValueError("No valid coin denominations")

    @cache
    def solve(t: int) -> int:
        if t == 0:
            return 0
        best_local = None
        for c in denoms:
            if c <= t:
                try:
                    candidate = 1 + solve(t - c)
                    best_local = (
                        candidate if best_local is None or candidate < best_local else best_local
                    )
                except ValueError:
                    pass
        if best_local is None:
            raise ValueError("No combination makes the target")
        return best_local

    return solve(target)
