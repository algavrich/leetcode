"""Given two strings ransomNote and magazine, return true if ransomNote can be
constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

>>> can_construct("a", "b")
False

>>> can_construct("aa", "ab")
False

>>> can_construct("aa", "aab")
True

"""

from collections import defaultdict


def can_construct(ransomNote: str, magazine: str) -> bool:
    """First, intuitive solution using two hash maps. Accepted."""
    ransom_dict = defaultdict(int)
    for ch in ransomNote:
        ransom_dict[ch] += 1
    mag_dict = defaultdict(int)
    for ch in magazine:
        mag_dict[ch] += 1
    for ch in ransom_dict:
        if ch in mag_dict and mag_dict[ch] >= ransom_dict[ch]:
            mag_dict[ch] -= ransom_dict[ch]
        else:
            return False
        
    return True


if __name__ == '__main__':
    import doctest
    doctest.testmod()