"""Given an array of integers arr, a lucky integer is an integer that has a
frequency in the array equal to its value.

Return the largest lucky integer in the array. If there is no lucky integer
return -1.

>>> find_lucky([2,2,3,4])
2

>>> find_lucky([1,2,2,3,3,3])
3

>>> find_lucky([2,2,2,3,3])
-1

"""

from typing import List
from collections import defaultdict


def find_lucky(arr: List[int]) -> int:
    """First, intuitive solution using hash map. Accepted."""

    counts = defaultdict(int)

    for num in arr:
        counts[num] += 1

    luckies = []
    for num in counts:
        if num == counts[num]:
            luckies.append(num)
            
    return max(luckies) if luckies else -1


def find_lucky(arr: List[int]) -> int:
    """Slightly faster solution manipulating original hash map instead of
    making new luckies array. Accepted.
    
    """

    counts = defaultdict(int)

    for num in arr:
        counts[num] += 1

    for num in arr:
        if num != counts[num]:
            del counts[num]

    return max(counts.keys()) if counts else -1


def find_lucky(arr: List[int]) -> int:
    """Inspired by another's solution, less space. Accepted."""

    counts = defaultdict(int)
    ans = -1

    for num in arr:
        counts[num] += 1

    for num, count in counts.items():
        if num == count and count > ans:
            ans = num
            
    return ans


if __name__ == '__main__':
    import doctest
    doctest.testmod()