"""Given a string date representing a Gregorian calendar date 
formatted as YYYY-MM-DD, return the day number of the year.

>>> day_of_year("2019-01-09")
9

>>> day_of_year("2019-02-10")
41

"""

from datetime import datetime


def day_of_year(date: str) -> int:
    """First, intuitive solution. Accepted."""

    days_of_months = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31,
    }
    
    days = 0
    
    for month in range(1, int(date[5:7].lstrip())):
        days += days_of_months[month]
        
    days += int(date[8:].lstrip())
    
    if int(date[:4]) % 4 == 0 and int(date[5:7].lstrip()) > 2:
        if int(date[:4]) % 400 == 0 or not int(date[:4]) % 100 == 0:
            days += 1  
        
    return days


def day_of_year(date: str) -> int:
    """'Cheat' solution using datetime module.
    Found in discussion. Accepted.
    
    """

    y, m, d = map(int, date.split("-"))
    return int((datetime(y, m, d) - datetime(y, 1, 1)).days + 1)


if __name__ == "__main__":
    import doctest
    doctest.testmod()