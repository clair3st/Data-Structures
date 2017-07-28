"""Implementation of a double linked list in Python."""


class Node(object):
    """Node class for data storage."""

    def __init__(self, data=None, next_node=None, prev=None):
        """Initialize Node."""
        self.data = data
        self.next = next_node
        self.prev = prev

    def __repr__(self):
        """String representation."""
        return "Value: {}".format(self.data)


class DoubleLinkedList(object):
    """Double linked list impplementation.

    Methods supported
    push(val) - will insert the value (val) at the head of the list
    append(val) - will append the value (val) at the tail of the list
    pop() - will pop the first val off the head of the list and return it.
    shift() - will remove the last val from the tail of the list and return it.
    remove(val) - will remove the first instance of (val) found in the list,
    starting from the head.
    """

    def __init__(self, data=None):
        """Initialize list."""
        self.head = None
        self.tail = None
        self._length = 0
        try:
            for val in data:
                self.push(val)
        except TypeError:
            if data:
                self.push(data)

    def push(self, val):
        """Add val to the head of the list."""
        old_head = self.head
        self.head = Node(val, next_node=old_head)
        if old_head:
            old_head.prev = self.head
        if not self.tail:
            self.tail = self.head
        self._length += 1

    def pop(self):
        """Remove the val from the head of the list."""
        to_return = self.head
        if self._length < 1:
            raise IndexError('Cannot pop from an empty list.')

        new_head = self.head.next
        if new_head:
            new_head.prev = None
        self.head = new_head
        self._length -= 1
        if self._length < 1:
            self.tail = None
        return to_return.data

    def append(self, val):
        """Add val to the tail of the list."""
        old_tail = self.tail
        self.tail = Node(val, prev=old_tail)
        if old_tail:
            old_tail.next = self.tail
        if self._length < 1:
            self.head = self.tail
        self._length += 1

    def shift(self):
        """Remove the val from the tail of the list."""
        to_return = self.tail
        if self._length < 1:
            raise IndexError('Cannot shift from an empty list.')

        new_tail = self.tail.prev
        if new_tail:
            new_tail.next = None
        self.tail = new_tail
        self._length -= 1
        if self._length < 1:
            self.tail = None
        return to_return.data

    def remove(self, val):
        """Remove first occurance of val from list."""
        curr = self.head
        while curr:
            if curr.data is val:
                if self._length is 1:
                    self.head, self.tail = None, None
                elif curr is not self.head and curr is not self.tail:
                    curr.next.prev, curr.prev.next = curr.prev, curr.next
                elif curr is self.head:
                    self.head, curr.next.prev = curr.next, None
                elif curr is self.tail:
                    self.tail, curr.prev.next = curr.prev, None
                self._length -= 1
                return
            curr = curr.next

        raise ValueError('{} is not in the list'.format(val))

    def _repr(self):
        """Return list representation of dll."""
        l = []
        while True:
            try:
                popped_data = self.pop()
                l.append(popped_data)
            except IndexError:
                break
        return l
