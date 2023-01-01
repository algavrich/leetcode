"""Given a string s, sort it in decreasing order based on the frequency of the
characters. The frequency of a character is the number of times it appears in
the string.

Return the sorted string. If there are multiple answers, return any of them.

>>> frequency_sort("tree")
'eetr'

>>> frequency_sort("cccaaa")
'cccaaa'

>>> frequency_sort("Aabb")
'bbAa'

"""

from collections import defaultdict


def frequency_sort(s: str) -> str:
    """First, intuitive solution using hash map. Accepted."""

    counts = defaultdict(int)

    for ch in s:
        counts[ch] += 1

    highest = max(counts.values())
    ans = []

    for i in range(highest, 0, -1):
        for ch, count in counts.items():
            if count == i:
                for j in range(count):
                    ans. append(ch)

    return "".join(ans)


def frequency_sort(s: str) -> str:
    """Improvement on previous solution using reverse sorting by length
    instead of third inner loop. Accepted.
    
    """
    counts = defaultdict(int)

    for ch in s:
        counts[ch] += 1

    ans = []

    for ch, count in counts.items():
        ans_part = []

        for i in range(count):
            ans_part.append(ch)
        ans.append("".join(ans_part))

    ans.sort(key=len, reverse=True)
    return "".join(ans)


if __name__ == '__main__':
    import doctest
    doctest.testmod()