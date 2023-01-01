"""You are given an integer array nums. The unique elements of an array are
the elements that appear exactly once in the array.

Return the sum of all the unique elements of nums.

>>> sum_of_unique([1,2,3,2])
4

>>> sum_of_unique([1,1,1,1,1])
0

>>> sum_of_unique([1,2,3,4,5])
15

"""

from typing import List
from collections import defaultdict


def sum_of_unique(nums: List[int]) -> int:
    """First, intuitive solution using hash map. Accepted."""

    counts = defaultdict(int)
    for num in nums:
        counts[num] += 1

    ans = 0
    for num in counts:
        if counts[num] == 1:
            ans += num

    return ans


def sum_of_unique(nums: List[int]) -> int:
    """Slightly faster solution using two hash sets. Accepted."""

    seen_once = set()
    more_than_once = set()

    for num in nums:
        if num in seen_once:
            seen_once.remove(num)
            more_than_once.add(num)
        elif num in more_than_once:
            continue
        else:
            seen_once.add(num)

    return sum(seen_once)


if __name__ == '__main__':
    import doctest
    doctest.testmod()