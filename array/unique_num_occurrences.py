"""Given an array of integers arr, return true if the number of occurrences
of each value in the array is unique or false otherwise.

>>> unique_occurrences([1,2,2,1,1,3])
True

>>> unique_occurrences([1,2])
False

"""

from typing import List
from collections import defaultdict


def unique_occurrences(arr: List[int]) -> bool:
    """First, intuitive solution using hash map. Accepted."""

    counts = defaultdict(int)

    for num in arr:
        counts[num] += 1

    counts_set = set(counts.values())

    return len(counts_set) == len(counts)


def unique_occurrences(arr: List[int]) -> bool:
    """Modified solution, slower but less space. Accepted."""

    counts = defaultdict(int)

    for num in arr:
        counts[num] += 1

    seen_counts = set()
    for count in counts.values():
        if count in seen_counts:
            return False
        else:
            seen_counts.add(count)

    return True


if __name__ == '__main__':
    import doctest
    doctest.testmod()