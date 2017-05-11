"""Testing binary Heap."""


import pytest


def test_node_has_data():
    """Test node object has data."""
    from src.binheap import Node
    bh = Node(None, 5)
    assert bh.data is 5
    assert bh.left is None and bh.right is None


def test_node_has_parent_and_children():
    """Test node object has parent and children."""
    from src.binheap import Node
    bh = Node(None, 5)
    assert bh.parent is None
    assert bh.left is None and bh.right is None
