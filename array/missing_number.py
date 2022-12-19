"""Given an array nums containing n distinct numbers in the range [0, n],
return the only number in the range that is missing from the array.

>>> missing_number([3,0,1])
2

>>> missing_number([0,1])
2

>>> missing_number([9,6,4,2,3,5,7,0,1])
8

"""

from typing import List

def missing_number(nums: List[int]) -> int:
    """Wrote this without converting nums to set. Obviously inefficient.
    This is my first, intuitive solution (plus set). Accepted.

    """

    nums = set(nums)

    for i in range(len(nums) + 1):
        if i not in nums:
            return i


def missing_number(nums: List[int]) -> int:
    """One of the official solutions using Gauss' formula."""

    expected_sum = len(nums) * (len(nums) + 1) / 2
    actual_sum = sum(nums)

    return int(expected_sum - actual_sum)


if __name__ == "__main__":
    import doctest
    doctest.testmod()

