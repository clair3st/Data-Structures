"""Python implementation of Binary Heap."""


class Node(object):
    """Node object of binary heap."""

    def __init__(self, parent, data=None, left=None, right=None):
        """Initialize a node."""
        self.left = left
        self.right = right
        self.parent = parent
        self.data = data


class Binheap(object):
    """Python implementation of binary heap.

    supports the following method

    push(): puts a new value into the heap, maintaining the heap property.
    pop(): removes the top value in the heap, maintaining the heap property.
    """

    def __init__(self, data=None):
        """Initialize bin heap."""
        self.head = None

    def push(self):
        """Put a new value into the heap."""
        pass

    def pop(self):
        """Remove the top value of the heap."""
        pass
