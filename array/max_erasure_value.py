"""You are given an array of positive integers nums and want to erase a
subarray containing unique elements. The score you get by erasing the subarray
is equal to the sum of its elements.

Return the maximum score you can get by erasing exactly one subarray.

>>> max_unique_subarray([4,2,4,5,6])
17

>>> max_unique_subarray([5,2,1,2,5,2,1,2,5])
8

"""

from typing import List
from collections import defaultdict


def max_unique_subarray(nums: List[int]) -> int:
    """First, intuitive solution using hash map and sliding window.
    Accepted.
    
    """

    num_counts = defaultdict(int)
    left = curr = ans = 0

    for right in range(len(nums)):
        curr += nums[right]
        num_counts[nums[right]] += 1

        while num_counts[nums[right]] > 1 and left < right:
            curr -= nums[left]
            num_counts[nums[left]] -= 1
            left += 1

        ans = max(ans, curr)

    return ans


def max_unique_subarray(nums: List[int]) -> int:
    """Modified solution, inspired by others' solutions. Uses hash set rather
    than hash map. Slightly faster but more space. Accepted.
    
    """

    seen = set()
    curr = ans = left = 0

    for right in range(len(nums)):
        while nums[right] in seen:
            curr -= nums[left]
            seen.remove(nums[left])
            left += 1

        curr += nums[right]
        seen.add(nums[right])
        ans = max(ans, curr)

    return ans


if __name__ == '__main__':
    import doctest
    doctest.testmod()