"""Given a string text, you want to use the characters of text to form as
many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number
of instances that can be formed.

>>> max_balloons("nlaebolko")
1

>>> max_balloons("loonbalxballpoon")
2

>>> max_balloons("leetcode")
0

"""


def max_balloons(text: str) -> int:
    """First, intuitive solution. Accepted."""

    letter_counts = {
        "b": 0,
        "a": 0,
        "l": 0,
        "o": 0,
        "n": 0,
    }

    for ch in text:
        if ch in letter_counts:
            letter_counts[ch] += 1
    
    return min(
        [
            letter_counts["b"],
            letter_counts["a"],
            int(letter_counts["l"]/2),
            int(letter_counts["o"]/2),
            letter_counts["n"],
        ]
    )


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    