"""Python implementation of a priorityq."""

from a_queue import Queue


class PriorityQ(object):
    """
    Priority Q data structure.

    Following methods are supported.

    Insert(value): inserts a value into the queue.
    Takes an optional argument for that value's priority.
    pop(): removes the most important item from the queue
    and returns its value.
    peek(): returns the most important item without removing it from the queue.
    """

    def __init__(self):
        """Initialize priorityq."""
        self._container = Queue()

    def insert(self, val, priority=0):
        """Insert a val into the queue with an argument for the priority."""
        self._container.push((val, priority))

    def pop(self):
        """Remove the most important item from the queue."""
        pass

    def peek(self):
        """Return the most important item without removing it."""
        pass
