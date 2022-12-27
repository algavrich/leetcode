"""Given a string s, reverse the string according to the following rules:

All the characters that are not English letters remain in the same position.
All the English letters (lowercase or uppercase) should be reversed.
Return s after reversing it.

>>> reverse_only_letters('ab-cd')
'dc-ba'

>>> reverse_only_letters('a-bC-dEf-ghIj')
'j-Ih-gfE-dCba'

>>> reverse_only_letters('Test1ng-Leet=code-Q!')
'Qedo1ct-eeLg=ntse-T!'

"""


def reverse_only_letters(s: str) -> str:
    """First, intuitive solution using two pointers. Accepted."""

    letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    s = list(s)

    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] in letters and s[right] in letters:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        elif s[left] not in letters:
            left += 1

        elif s[right] not in letters:
            right -= 1
            
    return "".join(s)


if __name__ == '__main__':
    import doctest
    doctest.testmod()