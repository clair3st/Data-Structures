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


def test_pop_reduces_length(test_lists):
    """Test pop reduces lists."""
    old_length = test_lists[2]._length
    test_lists[2].pop()
    assert test_lists[2]._length is old_length - 1


def test_pop_removes_head(test_lists):
    """Test pop removes head."""
    new_head = test_lists[2].head.next.data
    test_lists[2].pop()
    assert test_lists[2].head.data is new_head


def test_pop_removes_prev_pointer(test_lists):
    """Test pop changes prev pointer."""
    test_lists[2].pop()
    assert test_lists[2].head.prev is None


def test_pop_list_one(test_lists):
    """Test pop decreases length."""
    test_lists[1].pop()
    assert test_lists[1]._length is 0


def test_cant_pop_on_empty_list(test_lists):
    """Test pop on an empty list raises error."""
    with pytest.raises(IndexError, message='Cannot pop from an empty list'):
        test_lists[0].pop()


def test_append_increases_length(test_lists):
    """Test append increases length."""
    test_lists[0].append(2)
    assert test_lists[0]._length is 1


def test_append_updates_tail(test_lists):
    """Test append updates tail."""
    test_lists[1].append(6)
    assert test_lists[1].tail.data is 6


def test_append_points_back(test_lists):
    """Test old tail points to new with prev after a append."""
    old_tail = test_lists[1].tail
    test_lists[1].append(6)
    assert test_lists[1].tail is old_tail.prev
