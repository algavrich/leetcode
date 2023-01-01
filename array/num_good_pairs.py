"""Given an array of integers nums, return the number of good pairs.

A pair (i, j) is called good if nums[i] == nums[j] and i < j.

>>> num_pairs([1,2,3,1,1,3])
4

>>> num_pairs([1,1,1,1])
6

>>> num_pairs([1,2,3])
0

"""

from typing import List
from math import comb
from collections import defaultdict


def num_pairs(nums: List[int]) -> int:
    """First, intuitive solution using hash map and built-in combination
    function from math library. Accepted.
    
    """

    nums_map = defaultdict(list)

    for i in range(len(nums)):
        nums_map[nums[i]].append(i)

    count = 0

    for num in nums_map:
        list_len = len(nums_map[num])
        if list_len > 1:
            count += comb(list_len, 2)

    return int(count)


if __name__ == '__main__':
    import doctest
    doctest.testmod()