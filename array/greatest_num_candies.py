"""There are n kids with candies. You are given an integer array candies,
where each candies[i] represents the number of candies the ith kid has,
and an integer extraCandies, denoting the number of extra candies that you
have.

Return a boolean array result of length n, where result[i] is true if, after
giving the ith kid all the extraCandies, they will have the greatest number of
candies among all the kids, or false otherwise.

Note that multiple kids can have the greatest number of candies.

>>> kids_with_candies([2,3,5,1,3], 3)
[True, True, True, False, True]

>>> kids_with_candies([4,2,1,1,2], 1)
[True, False, False, False, False]

>>> kids_with_candies([12,1,12], 10)
[True, False, True]

"""

from typing import List


def kids_with_candies(candies: List[int], extra_candies: int) -> List[bool]:
    """Intuitive solution. Accepted."""

    richest_without_extra = max(candies)
    ans = []

    for i in range(len(candies)):
        ans.append(candies[i] + extra_candies >= richest_without_extra)

    return ans


def kids_with_candies(candies: List[int], extra_candies: int) -> List[bool]:
    """Inspired by another user's solution. Modifies candies in place. 
    Faster. Accepted.
    
    """

    richest_without_extra = max(candies)

    for i in range(len(candies)):
        candies[i] = candies[i] + extra_candies >= richest_without_extra

    return candies


if __name__ == '__main__':
    import doctest
    doctest.testmod()