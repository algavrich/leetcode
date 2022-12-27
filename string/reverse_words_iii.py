"""Given a string s, reverse the order of characters in each word within a
sentence while still preserving whitespace and initial word order.

>>> reverse_words("Lets take LeetCode contest")
'steL ekat edoCteeL tsetnoc'

>>> reverse_words("God Ding")
'doG gniD'

"""

def reverse_words(s: str) -> str:
    """First, intuitive solution. Accepted."""

    words = s.split()
    reversed_words = []

    for word in words:
        reversed_word = []

        for i in range(len(word) - 1, -1, -1):
            reversed_word.append(word[i])

        reversed_words.append("".join(reversed_word))

    return ' '.join(reversed_words)


def reverse_words(s: str) -> str:
    """Modified version of previous solution using two pointers. Accepted."""

    words = s.split()
    reversed_words = []

    for word in words:
        word = list(word)
        left = 0
        right = len(word) - 1

        while left < right:
            word[left], word[right] = word[right], word[left]
            left += 1
            right -= 1

        reversed_words.append("".join(word))
        
    return " ".join(reversed_words)


if __name__ == '__main__':
    import doctest
    doctest.testmod()