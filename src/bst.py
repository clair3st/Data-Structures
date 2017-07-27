"""Python implementation of Binary Search Tree."""


class Node(object):
    """Node, or leaf of the BST."""

    def __init__(self, val=None, parent=None):
        """Create node object."""
        self.val = val
        self.right = None
        self.left = None
        self.parent = parent
        self.depth = 0
        self.depth_level = 0

    def is_leaf(self):
        """Return True if node is a leaf (no children)."""
        return not (self.right and self.left)


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
        self.root = None
        self._depth = 0

        if data:
            for i in data:
                self.insert(i)

    def insert(self, val):
        """Insert val into BST. If val is already present will be ignored."""
        if not self.root:
            self.root = Node(val)
            self._size += 1
        else:
            self._sink(val, self.root)


        # branch_level = 0
        # while curr:
        #     branch_level += 1
        #     if val < curr.val:
        #         curr = self._set_child(curr, 'left', val, branch_level)
        #     elif val > curr.val:
        #         curr = self._set_child(curr, 'right', val, branch_level)
        #     else:
        #         break

    def _sink(self, val, curr):
        """Recursively inserts value into the tree."""
        if val < curr.val:
            # if not cur_node.left_child:
            #     cur_node.left_child = Node(val, cur_node)
            #     self.size_number += 1
            #     if cur_node.balance_number == 0:
            #         cur_node.balance_number = 1
            # else:
            #     count = self._sink(val, cur_node.left_child)
            #     if cur_node.balance_number <= count:
            #         cur_node.balance_number += 1
            curr = self._set_child(curr, 'left', val)

        elif val > curr.val:
            # if not cur_node.right_child:
            #     cur_node.right_child = Node(val, cur_node)
            #     self.size_number += 1
            #     if cur_node.balance_number == 0:
            #         cur_node.balance_number = 1
            # else:
            #     count = self._sink(val, cur_node.right_child)
            #     if cur_node.balance_number <= count:
            #         cur_node.balance_number += 1
            curr = self._set_child(curr, 'right', val)
        return curr.depth_level

    def _set_child(self, curr, side, val):
        """Helping."""
        child = getattr(curr, side)
        if child:
            count = self._sink(val, child)
            if curr.depth_level <= count:
                curr.depth_level += 1
        else:
            setattr(curr, side, Node(val, curr))
            self._size += 1
            if curr.depth_level is 0:
                curr.depth_level += 1
        return curr
        # if getattr(curr, side):
        #     curr = getattr(curr, side)


        #     # self._set_height(curr.depth, branch_level)
        #     # self._set_height(self._depth, branch_level)

        #     # print(str(curr.val) + ': ' + str(curr.depth))

        # else:
        #     setattr(curr, side, Node(val, curr))
        #     self._size += 1

        # return curr

    def _set_height(self, depth, branch_height):
        """Set new branch height."""
        if depth < branch_height:
            depth = branch_height

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
        # return max(self._rightbalance, self._leftbalance)
        return self._depth

    def contains(self, val):
        """Return true if val is in the bst."""
        return self.search(val) is not None

    def balance(self, tree=None):
        """Return an integer of how well the tree is balanced.

        Trees which are higher on the left than the right should return a
        positive value, trees which are higher on the right than the left
        should return a negative value. An ideally-balanced tree should
        return 0.
        """
        if not tree:
            tree = self.root
        return tree._rightbalance - tree._leftbalance


if __name__ == '__main__':
    print('BST')
    b = Bst([1, 2, 3, 4, 5])
    print('root', b.root.val)
