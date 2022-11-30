"""There is a programming language with only four operations
and one variable X:

++X and X++ increments the value of the variable X by 1.
--X and X-- decrements the value of the variable X by 1.
Initially, the value of X is 0.

Given an array of strings operations containing a list of operations,
return the final value of X after performing all the operations.

>>> final_value(["--X","X++","X++"])
1

>>> final_value(["++X","++X","X++"])
3

>>> final_value(["X++","++X","--X","X--"])
0

"""


def final_value(operations: list[str]) -> int:
    """First, intuitive solution. Accepted."""

    x = 0
    for operation in operations:
        if operation == "++X" or operation == "X++":
            x += 1
        else:
            x -= 1
    return x



def final_value(operations: list[str]) -> int:
    """Second solution, from discussion.
    
    Slower in runtime than first, but slightly less memory.
    
    """
    ops = {
        "++X": 1,
        "X++": 1,
        "--X": -1,
        "X--": -1,
    }
    
    return sum(ops[op] for op in operations)


if __name__ == "__main__":
    import doctest
    doctest.testmod()