"""A pangram is a sentence where every letter of the English alphabet appears
at least once.

Given a string sentence containing only lowercase English letters,
return true if sentence is a pangram, or false otherwise.

>>> is_pangram("thequickbrownfoxjumpsoverthelazydog")
True

>>> is_pangram("leetcode")
False

"""

def is_pagram(sentence: str) -> bool:
    """First, intuitive solution. Accepted."""

    alphabet = set("abcdefghijklmnopqrstuvwxyz")

    for char in sentence:
        if char in alphabet:
            alphabet.remove(char)

    return alphabet == set()


def is_pangram(sentence: str) -> bool:
    """Official solution."""

    sentence = set(sentence)
    
    return len(sentence) == 26