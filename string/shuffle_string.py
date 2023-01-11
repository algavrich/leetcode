"""You are given a string s and an integer array indices of the same length.
The string s will be shuffled such that the character at the ith position
moves to indices[i] in the shuffled string.

Return the shuffled string.

>>> shuffle_string("codeleet", [4, 5, 6, 7, 0, 2, 1, 3])
'leetcode'

>>> shuffle_string("abc", [0, 1, 2])
'abc'

"""

from typing import List


def shuffle_string(s: str, indices: List[int]) -> str:
    """First, intuitive solution. Accepted."""

    ans = [0] * len(s)

    for i in range(len(s)):
        ans[indices[i]] = s[i]

    return "".join(ans)


if __name__ == '__main__':
    import doctest
    doctest.testmod()