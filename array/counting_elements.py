"""Given an integer array arr, count how many elements x there are,
such that x + 1 is also in arr. If there are duplicates in arr,
count them separately.

>>> count_elements([1,2,3])
2

>>> count_elements([1,1,3,3,5,5,7,7])
0

"""

from typing import List

def count_elements(arr: List[int]) -> int:
    """First, intuitive solution. Accepted."""

    arr_set = set(arr)
    count = 0

    for num in arr:
        if num + 1 in arr_set:
            count += 1

    return count


if __name__ == "__main__":
    import doctest
    doctest.testmod()