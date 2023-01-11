"""International Morse Code defines a standard encoding where each letter is
mapped to a series of dots and dashes, as follows:

'a' maps to ".-",
'b' maps to "-...",
'c' maps to "-.-.", and so on.

Given an array of strings words where each word can be written as a
concatenation of the Morse code of each letter.

For example, "cab" can be written as "-.-..--...", which is the concatenation
of "-.-.", ".-", and "-...". We will call such a concatenation the
transformation of a word.

Return the number of different transformations among all words we have.

>>> unique_morse_representations(["gin", "zen", "gig", "msg"])
2

>>> unique_morse_representations(["a"])
1

"""

from typing import List


def unique_morse_representations(words: List[str]) -> int:
    """First, intuitive solution. Accepted. Faster than 99.81%."""

    codes = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..",
             ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.",
             "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
    transformations = set()

    for word in words:
        morse = []

        for ch in word:
            morse.append(codes[ord(ch) - 97])

        transformations.add("".join(morse))

    return len(transformations)


if __name__ == '__main__':
    import doctest
    doctest.testmod()