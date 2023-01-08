"""You are given an m x n integer grid accounts where accounts[i][j] is the
amount of money the ith customer has in the jth bank.
Return the wealth that the richest customer has.

A customer's wealth is the amount of money they have in all their bank
accounts. The richest customer is the customer that has the maximum wealth.

>>> maximum_wealth([[1,2,3],[3,2,1]])
6

>>> maximum_wealth([[1,5],[7,3],[3,5]])
10

>>> maximum_wealth([[2,8,7],[7,1,3],[1,9,5]])
17

"""

from typing import List


def maximum_wealth(accounts: List[List[int]]) -> int:
    """First, intuitive solution. Accepted."""

    richest = 0

    for i in range(len(accounts)):
        richest = max(richest, sum(accounts[i]))

    return richest

def maximum_wealth(accounts: List[List[int]]) -> int:
    """Improved solution, condensed into one line with inspiration from
    another user's solution. Faster runtime, same space. Accepted.
    
    """

    return max(sum(account) for account in accounts)


if __name__ == '__main__':
    import doctest
    doctest.testmod()