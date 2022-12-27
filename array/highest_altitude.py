"""There is a biker going on a road trip. The road trip consists
of n + 1 points at different altitudes. The biker starts his trip
on point 0 with altitude equal 0.

You are given an integer array gain of length n where gain[i]
is the net gain in altitude between points i​​​​​​ and i + 1 for all
(0 <= i < n). Return the highest altitude of a point.

>>> largest_altitude([-5,1,5,0,-7])
1

>>> largest_altitude([-4,-3,-2,-1,4,3,2])
0

"""

from typing import List


def largest_altitude(gain: List[int]) -> int:
    """First, intuitive solution using prefix sum. Accepted."""

    prefix = [gain[0]]

    for i in range(1, len(gain)):
        prefix.append(gain[i] + prefix[-1])

    return max([0] + prefix)


if __name__ == '__main__':
    import doctest
    doctest.testmod()