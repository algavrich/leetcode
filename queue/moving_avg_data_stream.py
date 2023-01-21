"""Given a stream of integers and a window size, calculate the moving average
of all integers in the sliding window.

Implement the MovingAverage class:

MovingAverage(int size) Initializes the object with the size of the window
size.
double next(int val) Returns the moving average of the last size values of
the stream.

>>> moving_average = MovingAverage(3)
>>> moving_average.next(1)
1.0
>>> moving_average.next(10)
5.5
>>> moving_average.next(3)
4.666666666666667
>>> moving_average.next(5)
6.0

"""

from collections import deque


class MovingAverage:
    """MovingAverage class."""

    def __init__(self, size: int):
        """Constructor for MovingAverage class."""

        self.queue = deque()
        self.size = size
        

    def next(self, val: int) -> float:
        """First, intuitive solution using a deque. Accepted."""

        if len(self.queue) > self.size-1:
            self.queue.popleft()

        self.queue.append(val)
        
        return sum(self.queue)/len(self.queue)
    

if __name__ == '__main__':
    import doctest
    doctest.testmod()