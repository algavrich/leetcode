"""Given a string path, where path[i] = 'N', 'S', 'E' or 'W',
each representing moving one unit north, south, east, or west,
respectively. You start at the origin (0, 0) on a 2D plane and
walk on the path specified by path.

Return true if the path crosses itself at any point, that is,
if at any time you are on a location you have previously visited.
Return false otherwise.

>>> is_path_crossing("NES")
False

>>> is_path_crossing("NESWW")
True

"""

from collections import defaultdict


def is_path_crossing(path: str) -> bool:
    """First, intuitive solution using hash map. Accepted."""

    visited = defaultdict(set)
    curr = [0, 0]
    visited[0].add(0)

    for ch in path:
        if ch == 'N':
            curr[1] += 1
        elif ch == 'S':
            curr[1] -= 1
        elif ch == 'E':
            curr[0] += 1
        else:
            curr[0] -= 1

        if curr[1] in visited[curr[0]]:
            return True
        else:
            visited[curr[0]].add(curr[1])

    return False


if __name__ == '__main__':
    import doctest
    doctest.testmod()