"""Implementation of Linked List in Python."""


class Node(object):
    """Node (data element) object.

    Data attribute for data storage and Next for pointer to next node.
    """

    def __init__(self, data, next_node=None):
        """Attribute data and next_node."""
        self.data = data
        self.next = next_node
