"""Python implementation of Binary Heap."""


class Binheap(object):
    """Python implementation of binary heap.

    supports the following method

    push(): puts a new value into the heap, maintaining the heap property.
    pop(): removes the top value in the heap, maintaining the heap property.
    """

    def __init__(self, data=None):
        """Initialize bin heap."""
        self.container = [None]

    def push(self, val):
        """Put a new value into the heap."""
        self.container.append(val)

    def pop(self):
        """Remove the top value of the heap."""
        pass
