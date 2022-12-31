"""You are given the array paths, where paths[i] = [cityAi, cityBi] means
there exists a direct path going from cityAi to cityBi. Return the destination
city, that is, the city without any path outgoing to another city.

It is guaranteed that the graph of paths forms a line without any loop,
therefore, there will be exactly one destination city.

>>> dest_city([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]])
'Sao Paulo'

>>> dest_city([["B","C"],["D","B"],["C","A"]])
'A'

>>> dest_city([["A","Z"]])
'Z'

"""

from typing import List


def dest_city(paths: List[List[str]]) -> str:
    """First, intuitive solution. Accepted."""

    start = set()
    end = set()

    for s, e in paths:
        start.add(s)
        end.add(e)

    for end_city in end:
        if end_city not in start:
            return end_city

def dest_city(paths: List[List[str]]) -> str:
    """Same thing but using set comprehension. Accepted."""

    start = {path[0] for path in paths}
    end = {path[1] for path in paths}

    for end_city in end:
        if end_city not in start:
            return end_city


if __name__ == '__main__':
    import doctest
    doctest.testmod()