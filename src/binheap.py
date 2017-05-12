"""Python implementation of Binary Heap."""


class Node(object):
    """Node object of binary heap."""

    def __init__(self, data=None, parent=None, left=None, right=None):
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

    def push(self, val):
        """Put a new value into the heap."""
        if not self.head:
            self.head = Node(val)
        else:
            curr = self.head
            while True:
                if curr.left and curr.right:
                    curr = curr.left
                elif curr.left:
                    curr.right = Node(val)
                    break
                else:
                    curr.left = Node(val)
                    break

    def pop(self):
        """Remove the top value of the heap."""
        pass
