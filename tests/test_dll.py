"""Test double linked list implementation."""

import pytest


@pytest.fixture
def test_lists():
    """Dll fixtures."""
    from src.dll import DoubleLinkedList
    empty = DoubleLinkedList()
    one = DoubleLinkedList(3)
    multi = DoubleLinkedList([1, 2, 3, 4, 5])
    return empty, one, multi


def test_node_class():
    """Test node class has data."""
    from src.dll import Node
    node = Node(5)
    assert node.data is 5


def test_list_of_none(test_lists):
    """Test list of none head and tail is none."""
    assert test_lists[0].head is None
    assert test_lists[0].tail is None


def test_list_of_one(test_lists):
    """Test list of one, head is tail."""
    assert test_lists[1].head is test_lists[1].tail


def test_list_of_five(test_lists):
    """Test list of five."""
    assert test_lists[2].head.data is 5
    assert test_lists[2].tail.data is 1


def test_prev_pointer(test_lists):
    """Test prev pointer."""
    assert test_lists[2].tail.prev.data is 2


def test_next_pointer(test_lists):
    """Test next pointer."""
    assert test_lists[2].head.next.data is 4


def test_push_increases_length(test_lists):
    """Test push increases length."""
    test_lists[0].push(2)
    assert test_lists[0]._length is 1


def test_push_updates_head(test_lists):
    """Test push updates head."""
    test_lists[1].push(6)
    assert test_lists[1].head.data is 6


def test_push_points_back(test_lists):
    """Test old head points to new with prev after a push."""
    old_head = test_lists[1].head
    test_lists[1].push(6)
    assert test_lists[1].head is old_head.prev
