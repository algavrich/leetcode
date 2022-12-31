"""Given an integer array nums, return true if any value appears at least
twice in the array, and return false if every element is distinct.

>>> contains_duplicate([1,2,3,1])
True

>>> contains_duplicate([1,2,3,4])
False

>>> contains_duplicate([1,1,1,3,3,4,3,2,4,2])
True

"""

from typing import List


def contains_duplicate(nums: List[int]) -> bool:
    """First, intuitive solution using hash set. Accepted."""

    seen = set()

    for num in nums:
        if num in seen:
            return True

        else:
            seen.add(num)

    return False


def containsDuplicate(self, nums: List[int]) -> bool:
    """Inspired by discussion solution. Slightly longer runtime, less memory.
    Accepted.
    
    """

    nums_set = set(nums)
    
    return len(nums_set) != len(nums)


if __name__ == '__main__':
    import doctest
    doctest.testmod()