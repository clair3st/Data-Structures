"""Testing binary Heap."""

import pytest


@pytest.fixture
def heap():
    """Fixture for heap."""
    from src.binheap import Binheap
    bh = Binheap()
    return bh


def test_node_has_data():
    """Test node object has data."""
    from src.binheap import Node
    node = Node(5)
    assert node.data is 5
    assert node.left is None and node.right is None


def test_node_has_parent_and_children():
    """Test node object has parent and children."""
    from src.binheap import Node
    node = Node(5)
    assert node.parent is None
    assert node.left is None and node.right is None


def test_push_val_to_head(heap):
    """Test push first val adds to the head."""
    heap.push(3)
    assert heap.head.data is 3


def test_push_val_to_left(heap):
    """Test push second val adds to the tree."""
    heap.push(3)
    heap.push(2)
    assert heap.head.left.data is 2


def test_push_val_to_right(heap):
    """Test push second val adds to the tree."""
    heap.push(10)
    heap.push(2)
    heap.push(5)
    assert heap.head.right.data is 5
