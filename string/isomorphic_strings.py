"""Given two strings s and t, determine if they are isomorphic.

   Two strings s and t are isomorphic if the characters in s can be replaced
   to get t.

   All occurrences of a character must be replaced with another character
   while preserving the order of characters. No two characters may map to 
   the same character, but a character may map to itself.
    
   >>> is_isomorphic("egg", "add")
   True

   >>> is_isomorphic("foo", "bar")
   False

   >>> is_isomorphic("paper", "title")
   True
   
   """


def is_isomorphic(s: str, t: str) -> bool:
    """First, intuitive solution. Accepted."""

    s_map = {}
    t_map = {}

    for i in range(len(s)):
        s_map[s[i]] = s_map.get(s[i], []) + [i]

    for j in range(len(t)):
        t_map[t[j]] = t_map.get(t[j], []) + [j]

    for indices in s_map.values():
        if indices not in t_map.values():
            return False

    return True


def is_isomorphic(s: str, t: str) -> bool:
    """Second solution, found in discussion. Accepted."""
    return len(set(zip(s, t))) == len(set(s)) == len(set(t))



if __name__ == '__main__':
    import doctest
    doctest.testmod()