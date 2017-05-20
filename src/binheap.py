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
        if data:
            for val in data:
                self.push(val)

    def push(self, val):
        """Put a new value into the heap."""
        self.container.append(val)
        size = len(self.container) - 1
        while size // 2 > 0:
            if self.container[size] > self.container[size // 2]:
                tmp = self.container[size // 2]
                self.container[size // 2] = self.container[size]
                self.container[size] = tmp
            size = size // 2

    def pop(self):
        """Remove the top value of the heap."""
        pass
