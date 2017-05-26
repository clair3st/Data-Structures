"""Stack implementation in Python."""

from src.linked_list import LinkedList


class Stack(object):
    """Implementation of Stack.

    public methods:

    push(value) - Adds a value to the stack.
    The parameter is the value to be added to the stack.
    pop() - Removes a value from the stack and returns that value.
    If the stack is empty, attempts to call pop should raise an exception.

    """

    def __init__(self, data=None):
        """Initialization."""
        self._stack = LinkedList(data)

    def push(self, val):
        """Add val to the stack."""
        self._stack.push(val)

    def pop(self):
        """Remove item off the stack."""
        self._stack.pop()
