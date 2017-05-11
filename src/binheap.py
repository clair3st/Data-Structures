"""Python implementation of Binary Heap."""


class Node(object):
    """Node object of binary heap."""

    def __init__(self, parent, data=None, left=None, right=None):
        """Initialize a node."""
        self.left = left
        self.right = right
        self.parent = parent
        self.data = data
