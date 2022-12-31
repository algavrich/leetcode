"""Given a string s, find the length of the longest substring without
repeating characters.

>>> longest_substring("abcabcbb")
3

>>> longest_substring("bbbbb")
1

>>> longest_substring("pwwkew")
3

"""

from collections import defaultdict


def longest_substring(s: str) -> int:
    """First, intuitive solution using sliding window and hash map.
    Accepted.
    
    """

    counts = defaultdict(int)
    left = ans = 0

    for right in range(len(s)):
        counts[s[right]] += 1

        while counts[s[right]] > 1:
            counts[s[left]] -= 1
            left += 1
            
        ans = max(ans, right - left + 1)

    return ans


if __name__ == '__main__':
    import doctest
    doctest.testmod()