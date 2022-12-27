"""Given a string s and an integer k, return the maximum number of
vowel letters in any substring of s with length k.

>>> max_vowels("abciiidef", 3)
3

>>> max_vowels("aeiou", 2)
2

>>> max_vowels("leetcode", 3)
2

"""


def max_vowels(s: str, k: int) -> int:
    """First, intuitive solution. Accepted."""

    vowels = set('aeiou')
    left = curr = ans = 0

    for i in range(k):
        if s[i] in vowels:
            curr += 1
    ans = curr

    for right in range(k, len(s)):
        if s[right] in vowels:
            curr += 1

        if s[left] in vowels:
            curr -= 1
        left += 1
        ans = max(ans, curr)

    return ans


if __name__ == '__main__':
    import doctest
    doctest.testmod()