"""Given a roman numeral, convert it to an integer.

   >>> roman_to_int("III")
   3

   >>> roman_to_int("LVIII")
   58

   >>> roman_to_int("MCMXCIV")
   1994

"""

def roman_to_int(s: str) -> int:
    translations = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }
    
    s = s.replace("IV", "IIII").replace("IX", "VIIII")
    s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
    s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
    
    num = 0
    for char in s:
        num += translations[char]
    
    return num



if __name__ == '__main__':
    import doctest
    from datetime import datetime
    start = datetime.now()
    doctest.testmod()
    print((datetime.now() - start).microseconds)