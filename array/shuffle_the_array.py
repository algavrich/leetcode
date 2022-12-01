"""Given the array nums consisting of 2n elements in the form
[x1,x2,...,xn,y1,y2,...,yn].

Return the array in the form [x1,y1,x2,y2,...,xn,yn].

>>> shuffle([2, 5, 1, 3, 4, 7], 3)
[2, 3, 5, 4, 1, 7]

>>> shuffle([1, 2, 3, 4, 4, 3, 2, 1], 4)
[1, 4, 2, 3, 3, 2, 4, 1]

>>> shuffle([1, 1, 2, 2], 2)
[1, 2, 1, 2]

"""


def shuffle(nums: list[int], n: int) -> list[int]:
    """First, intuitive solution. Accepted."""

    new_nums = []

    for i in range(n):
        new_nums.extend([nums[i], nums[n + i]])

    return new_nums

def shuffle(nums: list[int], n: int) -> list[int]:
    """Cool solution found in discussion. Accepted an efficient."""

    shuffled = []

    for i, j in zip(nums[:n], nums[n:]):
        shuffled += [i, j]
        
    return shuffled


if __name__ == "__main__":
    import doctest
    doctest.testmod()