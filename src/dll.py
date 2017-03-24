"""Implementation of a double linked list in Python."""


class Node(object):
    """Node class for data storage."""

    def __init__(self, data=None, next_node=None, prev=None):
        """Initialize Node."""
        self.data = data
        self.next = next_node
        self.prev = prev


class DoubleLinkedList(object):
    """Double linked list impplementation.

    Methods supported
    push(val) - will insert the value ‘val’ at the head of the list
    append(val) - will append the value ‘val’ at the tail of the list
    pop() - will pop the first val off the head of the list and return it.
    shift() - will remove the last val from the tail of the list and return it.
    remove(val) - will remove the first instance of ‘val’ found in the list,
    starting from the head.
    """

    def __init__(self, data=None, head=None, tail=None):
        """Initialize list."""
        self.head = head
        self.tail = tail
