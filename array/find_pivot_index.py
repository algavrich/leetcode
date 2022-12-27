"""Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly
to the left of the index is equal to the sum of all the numbers strictly
to the index's right.

If the index is on the left edge of the array, then the left sum is 0
because there are no elements to the left. This also applies to the right
edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.

>>> pivot_index([1,7,3,6,5,6])
3

>>> pivot_index([1,2,3])
-1

>>> pivot_index([2,1,-1])
0

"""

from typing import List


def pivot_index(nums: List[int]) -> int:
    """First, intuitive brute force solution.
    Accepted. Not runtime efficient.
    
    """

    for i in range(len(nums)):
        if sum(nums[:i]) == sum(nums[i + 1:]):
            return i

    return -1


def pivot_index(nums: List[int]) -> int:
    """Second solution using two integer variables for sums.
    Accepted. Average efficiency for runtime and memory.
    
    """

    left, right = 0, sum(nums)

    for i in range(len(nums)):
        right -= nums[i]

        if right == left:
            return i

        left += nums[i]
        
    return -1


def pivot_index(nums: List[int]) -> int:
    """My best solution. Uses prefix sum. Accepted."""

    prefix = [nums[0]]

    for i in range(1, len(nums)):
        prefix.append(nums[i] + prefix[-1])

    if prefix[-1] - prefix[0] == 0:
        return 0

    for i in range(1, len(nums)):
        if prefix[i - 1] == prefix[-1] - prefix[i]:
            return i

    return -1


if __name__ == '__main__':
    import doctest
    doctest.testmod()