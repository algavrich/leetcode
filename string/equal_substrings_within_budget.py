"""You are given two strings s and t of the same length and an integer maxCost.

You want to change s to t. Changing the ith character of s to ith
character of t costs |s[i] - t[i]| (i.e., the absolute difference
between the ASCII values of the characters).

Return the maximum length of a substring of s that can be changed to be the
same as the corresponding substring of t with a cost less than or equal to
maxCost. If there is no substring from s that can be changed to its
corresponding substring from t, return 0.

>>> equal_substring("abcd", "bcdf", 3)
3

>>> equal_substring("abcd", "cdef", 3)
1

>>> equal_substring("abcd", "acde", 0)
1

"""


def equal_substring(s: str, t: str, max_cost: int) -> int:
        left = curr = ans = 0

        for right in range(len(s)):
            curr += abs(ord(s[right]) - ord(t[right]))

            while curr > max_cost:
                curr -= abs(ord(s[left]) - ord(t[left]))
                left += 1

            ans = max(ans, right - left + 1)

        return ans


if __name__ == '__main__':
    import doctest
    doctest.testmod()