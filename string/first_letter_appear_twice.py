"""Given a string s consisting of lowercase English letters,
return the first letter to appear twice.

Note:

A letter a appears twice before another letter b if the second occurrence
of a is before the second occurrence of b.
s will contain at least one letter that appears twice.

>>> repeated_character("abccbaacz")
'c'

>>> repeated_character("abcdd")
'd'

"""


def repeated_character(s: str) -> str:
    """First, intuitive solution. Accepted.
    
    Really proud of this one. 97.07% runtime, 95.28% memory.

    """

    counted_once = set()
    for char in s:
        if char in counted_once:
            return char
        counted_once.add(char)


if __name__ == "__main__":
    import doctest
    doctest.testmod()