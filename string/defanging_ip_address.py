"""Given a valid (IPv4) IP address, return a defanged version
of that IP address.

A defanged IP address replaces every period "." with "[.]".

>>> defang("1.1.1.1")
'1[.]1[.]1[.]1'

>>> defang("255.100.50.0")
'255[.]100[.]50[.]0'

"""


def defang(address: str) -> str:
    """First, intuitive solution. Accepted."""

    return address.replace(".", "[.]")


def defang(address: str) -> str:
    """Second solution, found in discussion.
    
    More efficient for both space and time.

    """

    return "[.]".join(address.split("."))



if __name__ == '__main__':
    import doctest
    doctest.testmod()