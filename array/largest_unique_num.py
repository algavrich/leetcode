"""Given an integer array nums,
return the largest integer that only occurs once.
If no integer occurs once, return -1.

>>> largest_unique_number([5,7,3,9,4,9,8,3,1])
8

>>> largest_unique_number([9,9,8,8])
-1

"""

from typing import List


def largest_unique_number(nums: List[int]) -> int:
    """First, intuitive solution using hash sets. Accepted."""

    occurs_once = set()
    more_than_once = set()
    
    for num in nums:
        if num in occurs_once:
            occurs_once.remove(num)
            more_than_once.add(num)

        elif num in more_than_once:
            continue

        else:
            occurs_once.add(num)

    if not occurs_once:
        return -1

    else:
        return max(occurs_once)


def largest_unique_number(nums: List[int]) -> int:
    """Inspired by official solution(uses hash map). Accepted."""

    counts = {}
    ans = -1
    
    for num in nums:
        counts[num] = counts.get(num, 0) + 1
        
    for num, count in counts.items():
        if count == 1:
            ans = max(ans, num)
    
    return ans


if __name__ == '__main__':
    import doctest
    doctest.testmod()