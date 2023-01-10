"""There is a hidden integer array arr that consists of n non-negative
integers.

It was encoded into another integer array encoded of length n - 1, such that
encoded[i] = arr[i] XOR arr[i + 1]. For example, if arr = [1,0,2,1], then
encoded = [1,2,3].

You are given the encoded array. You are also given an integer first, that is
the first element of arr, i.e. arr[0].

Return the original array arr. It can be proved that the answer exists and is
unique.

>>> decode([1,2,3], 1)
[1, 0, 2, 1]

>>> decode([6,2,7,3], 4)
[4, 2, 0, 7, 4]

"""

from typing import List


def decode(encoded: List[int], first: int) -> List[int]:
    """First, intuitive solution. Very dumb to use unreferenced i AND
    curr pointer. Accepted.
    
    """
    
    arr = [first]
    curr = 0

    for i in range(len(encoded)):
        arr.append(encoded[curr] ^ arr[-1])
        curr += 1

    return arr


def decode(encoded: List[int], first: int) -> List[int]:
    """Much saner and faster solution. Accepted."""

    arr = [first]

    for num in encoded:
        arr.append(num ^ arr[-1])

    return arr


if __name__ == '__main__':
    import doctest
    doctest.testmod()