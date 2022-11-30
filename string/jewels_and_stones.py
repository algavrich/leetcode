"""You're given strings jewels representing the types of stones
that are jewels, and stones representing the stones you have.
Each character in stones is a type of stone you have. You want to know
how many of the stones you have are also jewels.

Letters are case sensitive, so "a" is considered a different type of 
stone from "A".

>>> num_jewels("aA", "aAAbbbb")
3

>>> num_jewels("z", "ZZ")
0

"""


def num_jewels(jewels: str, stones:str) -> int:
    """First, intuitive solution. Accepted."""

    jewels = set(jewels)
    count = 0

    for stone in stones:
        if stone in jewels:
            count += 1
            
    return count


def num_jewels(jewels: str, stones:str) -> int:
    """Second solution. Tried to be clever, not as efficient."""

    jewels = set(jewels)

    return sum(1 for stone in stones if stone in jewels)



if __name__ == "__main__":
    import doctest
    doctest.testmod()