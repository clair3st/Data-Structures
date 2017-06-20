"""Python implementation of Binary Heap."""


class Binheap(object):
    """Python implementation of max binary heap.

    supports the following method

    push(): puts a new value into the heap, maintaining the heap property.
    pop(): removes the top value in the heap, maintaining the heap property.
    dislplay(): displays the heap as a string representation of a tree.
    """

    def __init__(self, data=None):
        """Initialize bin heap."""
        self.container = [None]
        if data:
            for val in data:
                self.push(val)

    def _balance(self):
        """Helper function to balance heap."""
        size = len(self.container) - 1
        while size // 2 > 0:
            if self.container[size] > self.container[size // 2]:
                tmp = self.container[size // 2]
                self.container[size // 2] = self.container[size]
                self.container[size] = tmp
            size = size // 2

    def push(self, val):
        """Put a new value into the heap."""
        self.container.append(val)
        self._balance()

    def pop(self):
        """Remove the top value of the heap."""
        if not self.container:
            raise IndexError('Can\'t pop from and empty heap')
        self.container.pop(1)
        self._balance()

    def display(self):
        """Display the heap as a tree."""
        cols = []
        col = 1
        to_show = ''
        l = self.container[1:]

        while len(self.container) > col:
            cols.append(col)
            col *= 2

        for i, v in enumerate(cols):
            buff = cols[-1 - i] // 2
            to_show += buff * ' '
            for idx in range(v):
                if l:
                    to_show += str(l.pop(0)) + ' '
            to_show += '\n'

        return to_show
