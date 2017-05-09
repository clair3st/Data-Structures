"""Python implementation of a deque."""

from dll import DoubleLinkedList


class Deque(object):
    """Deque data structure.

    Supports the following methods
    append(val): adds value to the end of the deque
    appendleft(val): adds a value to the front of the deque
    pop(): removes a value from the end of the deque and returns it (raises
    an exception if the deque is empty)
    popleft(): removes a value from the front of the deque and returns it
    (raises an exception if the deque is empty)
    peek(): returns the next value that would be returned by pop but leaves
    the value in the deque (returns None if the deque is empty)
    peekleft(): returns the next value that would be returned by popleft but
    leaves the value in the deque (returns None if the deque is empty)
    size(): returns the count of items in the queue (returns 0 if the queue
    is empty).
    """

    def __init__(self, data=None):
        """Initialize deque."""
        self._container = DoubleLinkedList(data)

    def append(self, val):
        """Add value to the end of the deque."""
        self._container.append(val)

    def appendleft(self, val):
        """Add a value to the front of the deque."""
        self._container.push(val)

    def pop(self):
        """Remove a value from the end of the deque and returns it."""
        return self._container.shift()

    def popleft(self):
        """Remove a value from the front of the deque and returns it."""
        return self._container.pop()

    def peek(self):
        """Return the next value that would be returned by pop."""
        if self._container.head:
            return self._container.head.data
        return None

    def peekleft(self):
        """Return the next value from the front of the deque."""
        if self._container.tail:
            return self._container.tail.data
        return None

    def size(self):
        """Return the count of items in the queue."""
        return self._container._length
