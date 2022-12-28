"""You are given an integer array matches where matches[i] = [winneri, loseri]
indicates that the player winneri defeated player loseri in a match.

Return a list answer of size 2 where:

answer[0] is a list of all players that have not lost any matches.
answer[1] is a list of all players that have lost exactly one match.
The values in the two lists should be returned in increasing order.

Note:

You should only consider the players that have played at least one match.
The testcases will be generated such that no two matches will have the same 
outcome.

>>> find_winners([[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]])
[[1, 2, 10], [4, 5, 7, 8]]

>>> find_winners([[2,3],[1,3],[5,4],[6,4]])
[[1, 2, 5, 6], []]

"""

from typing import List


def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
    """First, intuitive solution using hash map. Accepted."""

    counts = {}
    ans = [[], []]

    for match in matches:
        if match[0] not in counts:
            counts[match[0]] = [1, 0]

        else:
            counts[match[0]][0] += 1

        if match[1] not in counts:
            counts[match[1]] = [0, 1]

        else:
            counts[match[1]][1] += 1

    for player, scores in counts.items():
        if scores[1] == 0:
            ans[0].append(player)

        elif scores[1] == 1:
            ans[1].append(player)

    ans[0].sort()
    ans[1].sort()
    
    return ans


def find_winners(matches: List[List[int]]) -> List[List[int]]:
    """Slightly more efficient (official) solution. Obviously accepted."""

    zero_losses = set()
    one_loss = set()
    more_losses = set()

    for winner, loser in matches:
        if winner not in one_loss and winner not in more_losses:
            zero_losses.add(winner)

        if loser in zero_losses:
            zero_losses.remove(loser)
            one_loss.add(loser)

        elif loser in one_loss:
            one_loss.remove(loser)
            more_losses.add(loser)

        elif loser in more_losses:
            continue

        else:
            one_loss.add(loser)

    return [sorted(list(zero_losses)), sorted(list(one_loss))]


if __name__ == '__main__':
    import doctest
    doctest.testmod()