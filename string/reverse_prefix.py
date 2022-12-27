"""Given a 0-indexed string word and a character ch, reverse the segment of
word that starts at index 0 and ends at the index of the first occurrence of
ch (inclusive). If the character ch does not exist in word, do nothing.

>>> reverse_prefix("abcdefd", "d")
'dcbaefd'

>>> reverse_prefix("xyxzxe", "z")
'zxyxxe'

>>> reverse_prefix("abcd", "z")
'abcd'

"""


def reverse_prefix(word: str, ch: str) -> str:
    """First, intuitive solution using find method and two-pointers.
    Accepted.
    
    """

    ch_idx = word.find(ch)

    if ch_idx == -1:
        return word

    word = list(word)
    left = 0
    right = ch_idx

    while left < right:
        word[left], word[right] = word[right], word[left]
        left += 1
        right -= 1

    return "".join(word)



def reverse_prefix(word: str, ch: str) -> str:
    """Second (more efficient) solution using right pointer instead of
    find method. Accepted.
    
    """

    left = 0
    right = 0

    while word[right] != ch:
        if right == len(word) - 1:
            return word

        right += 1

    word = list(word)

    while left < right:
        word[left], word[right] = word[right], word[left]
        left += 1
        right -= 1

    return "".join(word)


if __name__ == '__main__':
    import doctest
    doctest.testmod()