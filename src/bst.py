"""Python implementation of Binary Search Tree."""


class Node(object):
    """Node, or leaf of the BST."""

    def __init__(self, val=None, parent=None):
        """Create node object."""
        self.val = val
        self.right = None
        self.left = None
        self.parent = parent


class Bst(object):
    """Binary Search Tree.

    Binary Search tree supports the following methods:

    insert(val): will insert the value val into the BST. If val is
     already present, it will be ignored.

    search(val): will return the node containing that value, else None

    size(): will return the integer size of the BST (equal to the total
    no. of values stored in the tree). It will return 0 if the tree is empty.

    depth(): will return an integer representing the total number of
    levels in the tree. If there are no values, depth is 0, if one value the
    depth should be 1, if two values it will be 2, if three values it may be
    2 or 3, depending, etc.

    contains(val): will return True if val is in the BST, False if not.

    balance(): will return an integer, positive or negative that represents
    how well balanced the tree is. Trees which are higher on the left than
    the right should return a positive value, trees which are higher on the
    right than the left should return a negative value. An ideally-balanced
    tree should return 0.
    """

    def __init__(self, data=None):
        """Initialize tree."""
        self._size = 0
        self._rightbalance = 0
        self._leftbalance = 0
        self.root = None

        if data:
            for i in data:
                self.insert(i)

    def insert(self, val):
        """Insert val into BST. If val is already present will be ignored."""
        if not self.root:
            self.root = Node(val)
            self._size += 1
            return

        curr = self.root
        branch_level = 0
        while curr:
            branch_level += 1
            if val < curr.val:
                curr = self._set_child(curr, 'left', val, branch_level)
            elif val > curr.val:
                curr = self._set_child(curr, 'right', val, branch_level)
            else:
                break

    def _set_child(self, curr, side, val, branch_level):
        """Helping."""
        if getattr(curr, side):
            curr = getattr(curr, side)
        else:
            setattr(curr, side, Node(val, curr))
            self._size += 1

            if getattr(self, '_' + side + 'balance') < branch_level:
                setattr(self, '_' + side + 'balance', branch_level)

        return curr

    def search(self, val):
        """Return the node containing val."""
        curr = self.root
        while curr:
            if curr.val == val:
                return curr
            elif val < curr.val:
                curr = curr.left
            else:
                curr = curr.right

    def size(self):
        """Return the size of the BST."""
        return self._size

    def depth(self):
        """Return depth of the BST, representing total levels."""
        return max(self._rightbalance, self._leftbalance)

    def contains(self, val):
        """Return true if val is in the bst."""
        return self.search(val) is not None

    def balance(self):
        """Return an integer of how well the tree is balanced.

        Trees which are higher on the left than the right should return a
        positive value, trees which are higher on the right than the left
        should return a negative value. An ideally-balanced tree should
        return 0.
        """
        return self._rightbalance - self._leftbalance
