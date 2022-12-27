"""Given an integer array nums, move all 0's to the end of it while
maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

>>> move_zeroes([0,1,0,3,12])
[1,3,12,0,0]

>>> move_zeroes([0])
[0]

"""

from typing import List


def moveZeroes(self, nums: List[int]) -> None:
    """First, intuitive solution using two-pointers. Accepted."""

    left = 0
    right = len(nums) - 1

    while left < right:
        if nums[left] == 0:
            nums.append(nums.pop(left))
            right -= 1

        else:
            left += 1


if __name__ == '__main__':
    import doctest
    doctest.testmod()