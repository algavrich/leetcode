"""A sentence is a list of words that are separated by a single space 
with no leading or trailing spaces.

You are given an array of strings sentences, where each sentences[i]
represents a single sentence.

Return the maximum number of words that appear in a single sentence.

>>> most_words_found(["alice and bob love leetcode", "i think so too", "this is great thanks very much"])
6

>>> most_words_found(["please wait", "continue to fight", "continue to win"])
3

"""


def most_words_found(sentences: list[str]) -> int:
    """First, intuitive solution. Accepted."""

    sentences_split = []
    for sentence in sentences:
        sentences_split.append(sentence.split())

    longest = 0
    for split_sentence in sentences_split:
        longest = max(len(split_sentence), longest)

    return longest


def most_words_found(sentences: list[str]) -> int:
    """Second, more clever solution. More efficient runtime. Accepted."""
    
    longest = 0

    for sentence in sentences:
        current_length = sentence.count(" ") + 1
        longest = max(current_length, longest)
        
    return longest


if __name__ == "__main__":
    import doctest
    doctest.testmod()