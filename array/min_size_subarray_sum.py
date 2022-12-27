"""Given an array of positive integers nums and a positive integer target,
return the minimal length of a subarray whose sum is greater than or equal
to target. If there is no such subarray, return 0 instead.

>>> min_subarray_len(7, [2,3,1,2,4,3])
2

>>> min_subarray_len(4, [1,4,4])
1

>>> min_subarray_len(11, [1,1,1,1,1,1,1,1])
0

"""

from typing import List
from math import inf


def min_subarray_len(target: int, nums: List[int]) -> int:
    """First, intuitive solution. Accepted."""

    left = curr = 0
    ans = inf

    for right in range(len(nums)):
        curr += nums[right]

        while curr >= target:
            ans = min(ans, right - left + 1)
            curr -= nums[left]
            left += 1

    return 0 if ans == inf else ans


if __name__ == '__main__':
    import doctest
    doctest.testmod()