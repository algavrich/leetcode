"""Given two strings s and t, return true if s is a subsequence of t,
   or false otherwise.

   A subsequence of a string is a new string that is formed from
   the original string by deleting some (can be none) of the characters
   without disturbing the relative positions of the remaining characters.
   (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
   
   >>> is_subsequence("abc", "ahbgdc")
   True

   >>> is_subsequence("axc", "ahbgdc")
   False

   >>> is_subsequence("", "ahbgdc")
   True

   >>> is_subsequence("abc", "")
   False

   """

from datetime import datetime

def is_subsequence(s: str, t: str) -> bool:
    i, j = 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    return i == len(s)


def is_subsequence(s: str, t: str) -> bool:
    return all(c in t for c in s)



if __name__ == '__main__':
    import doctest
    start = datetime.now()
    doctest.testmod()
    print(datetime.now() - start)
