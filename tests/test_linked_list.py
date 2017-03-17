"""Test implementation of a linked list."""

import sys
import os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')


def test_node_has_data():
    """Test node object has data."""
    from src.linked_list import Node
    ll = Node(5)
    assert ll.data is 5
