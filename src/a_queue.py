"""Implementation of a queue in python."""


from src.dll import DoubleLinkedList


class Queue(object):
    """Implementation of Queue.

    This implementation supports the following public methods:
    enqueue(value): adds value to the queue
    dequeue(): removes the correct item from the queue and returns its value
    (should raise an error if the queue is empty)
    peek(): returns the next value in the queue without dequeueing it.
    If the queue is empty, returns None
    size(): return the size of the queue. Returns 0 if the queue is empty.
    """

    def __init__(self, data=None):
        """Initialize queue data structure."""
        self._container = DoubleLinkedList(data)

    def enqueue(self, val):
        """Add a value to the queue."""
        self._container.append(val)

    def dequeue(self):
        """Remove a value from the front of the queue."""
        return self._container.pop()

    def peek(self):
        """Return the next value in the queue without dequing it."""
        try:
            return self._container.head.data
        except AttributeError:
            return None

    def size(self):
        """Return the size of the queue."""
        return self._container._length
