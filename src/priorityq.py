"""Python implementation of a priorityq."""

from binheap import Binheap


class PriorityQ(object):
    """
    Priority Q data structure.

    Following methods are supported.

    Insert(value, [priority]): inserts a value into the queue.
    Takes an optional argument for that value's priority.
    pop(): removes the most important item from the queue
    and returns its value.
    peek(): returns the most important item without removing it from the queue.
    """

    def __init__(self):
        """Initialize priorityq."""
        self._container = Binheap()

    def insert(self, val, priority=0):
        """Insert a val into the queue with an argument for the priority."""
        self._container.push((priority, val))

    def pop(self):
        """Remove the most important item from the queue."""
        to_return = self._container.container[1][1]
        if not to_return:
            raise(IndexError, 'Can\'t pop from an empty queue.')
        self._container.pop()
        return to_return

    def peek(self):
        """Return the most important item without removing it."""
        try:
            return self._container.container[1][1]
        except IndexError:
            return None
