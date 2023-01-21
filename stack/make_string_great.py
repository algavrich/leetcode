"""Given a string s of lower and upper case English letters.

A good string is a string which doesn't have two adjacent characters
s[i] and s[i + 1] where:

0 <= i <= s.length - 2
s[i] is a lower-case letter and s[i + 1] is the same letter but in upper-case
or vice-versa.

To make the string good, you can choose two adjacent characters that make the
string bad and remove them. You can keep doing this until the string becomes
good.

Return the string after making it good. The answer is guaranteed to be unique
under the given constraints.

Notice that an empty string is also good.

>>> make_good('leEeetcode')
'leetcode'

>>> make_good('abBAcC')
''

>>> make_good('s')
's'

"""

def make_good(s: str) -> str:
    """Initial solution using dictionary to map lower to upper case letters.
    Accepted.
    
    """

    letters = {
        'a': 'A',
        'b': 'B',
        'c': 'C',
        'd': 'D',
        'e': 'E',
        'f': 'F',
        'g': 'G',
        'h': 'H',
        'i': 'I',
        'j': 'J',
        'k': 'K',
        'l': 'L',
        'm': 'M',
        'n': 'N',
        'o': 'O',
        'p': 'P',
        'q': 'Q',
        'r': 'R',
        's': 'S',
        't': 'T',
        'u': 'U',
        'v': 'V',
        'w': 'W',
        'x': 'X',
        'y': 'Y',
        'z': 'Z',
    }

    stack = []

    for c in s:
        if not stack:
            stack.append(c)

        else:
            if ((c in letters and letters[c] == stack[-1])
            or (stack[-1] in letters and letters[stack[-1]] == c)):
                stack.pop()

            else:
                stack.append(c)
                
    return ''.join(stack)


def make_good(s: str) -> str:
    """Second solution using lower() and upper() string methods to check for
    pairs. Accepted.
    
    """

    stack = []

    for c in s:
        if (stack 
            and (c != stack[-1]
            and (c.lower() == stack[-1] or c.upper() == stack[-1]))):
            stack.pop()

        else:
            stack.append(c)
                
    return ''.join(stack)



def make_good(s: str) -> str:
    """Taken from official solution. Uses ord() function to compare ASCII
    values. Accepted.
    
    """

    stack = []
    
    for c in s:
        if (stack and abs(ord(c) - ord(stack[-1])) == 32):
            stack.pop()

        else:
            stack.append(c)
                
    return ''.join(stack)


if __name__ == '__main__':
    import doctest
    doctest.testmod()