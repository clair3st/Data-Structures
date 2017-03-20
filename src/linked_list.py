"""Implementation of Linked List in Python."""


class Node(object):
    """Node (data element) object.

    Data attribute for data storage and Next for pointer to next node.
    """

    def __init__(self, data, next_node=None):
        """Attribute data and next_node."""
        self.data = data
        self.next = next_node


class LinkedList(object):
    """Method for linked list.

    push(val) - will insert the value at the head of the list.
    pop() - remove the first value off the head and return it.
    size() - will return the length of the list.
    search(val) - will return the node containing val in the list, if
    present, else None
    remove(node) - will remove the given node from the list, wherever
     it might be (node must be an item in the list)
    display() - will return a unicode string representing the list as
    if it were a Python tuple literal: "(12, 'sam', 37, 'tango')"
    """

    def __init__(self, data=None):
        """Linked list initialized with head."""
        self._length = 0
        self.head = None
        try:
            for val in data:
                self.push(val)
        except TypeError:
            if data:
                self.push(data)

    def push(self, val):
        """Insert a value at the head of the list."""
        old_head = self.head
        self.head = Node(val, old_head)
        self._length += 1

    def pop(self):
        """Remove the first value and return it."""
        if not self.head:
            raise IndexError('Cannot pop from an empty list')
        to_return = self.head
        self.head = self.head.next
        self._length -= 1
        return to_return.data

    def size(self):
        """Return the length of the list."""
        return self._length

    def search(self, val):
        """Return the node containing val."""
        curr = self.head
        while curr:
            if curr.data == val:
                return curr
            curr = curr.next

    def remove(self, val):
        """Remove node from list if exists."""
        curr = self.head
        if curr and val is self.head.data:
            self.head = self.head.next
            self._length -= 1
        while curr:
            if (curr.next and curr.next.data == val):
                curr.next = curr.next.next
                self._length -= 1
            curr = curr.next

    def display(self):
        """Display list as a tuple."""
        curr = self.head
        display = '('
        while curr:
            display += str(curr.data) + ', '
            curr = curr.next
        return display[:-2] + ')'
