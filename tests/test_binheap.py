"""Testing binary Heap."""


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


def test_push_val_to_head():
    """Test push first val adds to the head."""
    from src.binheap import Binheap
    bh = Binheap()
    bh.push(3)
    assert bh.head.data is 3
