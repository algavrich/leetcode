"""Given an integer array nums, handle multiple queries of the following type:

Calculate the sum of the elements of nums between indices left and right
inclusive where left <= right.

Implement the NumArray class:

NumArray(int[] nums) Initializes the object with the integer array nums.
int sumRange(int left, int right) Returns the sum of the elements of nums
between indices left and right inclusive
(i.e. nums[left] + nums[left + 1] + ... + nums[right]).

>>> num_array = NumArray([-2, 0, 3, -5, 2, -1])
>>> num_array.sumRange(0, 2)
1
>>> num_array.sumRange(2, 5)
-1
>>> num_array.sumRange(0, 5)
-3

"""

from typing import List


class NumArray:
    """Array of numbers."""

    def __init__(self, nums: List[int]):
        """Constructor for NumArray object."""

        self.nums = nums

        self.prefix = [nums[0]]
        if len(nums) > 1:
            for i in range(1, len(nums)):
                self.prefix.append(self.nums[i] + self.prefix[-1])

    def sumRange(self, left: int, right: int) -> int:
        """Return sum of range between left and right."""

        return self.prefix[right] - self.prefix[left] + self.nums[left]


if __name__ == '__main__':
    import doctest
    doctest.testmod()