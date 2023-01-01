"""Given a binary array nums and an integer goal, return the number of
non-empty subarrays with a sum goal.

A subarray is a contiguous part of the array.

>>> num_subarrays([1,0,1,0,1], 2)
4

>>> num_subarrays([0,0,0,0,0], 0)
15

"""

from typing import List
from collections import defaultdict, Counter


def num_subarrays(nums: List[int], goal: int) -> int:
    """First, intuitive solution using hash map. Accepted."""

    counts = defaultdict(int)
    counts[0] = 1
    ans = curr = 0

    for num in nums:
        curr += num
        ans += counts[curr - goal]
        counts[curr] += 1

    return ans


def num_subarrays(nums: List[int], goal: int) -> int:
    """Inspired by others' solutions. Uses Counter object. Accepted."""

    counts = Counter({0: 1})
    curr = ans = 0

    for num in nums:
        curr += num
        ans += counts[curr - goal]
        counts[curr] += 1

    return ans


if __name__ == '__main__':
    import doctest
    doctest.testmod()