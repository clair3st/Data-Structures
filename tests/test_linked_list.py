"""Test implementation of a linked list."""

import sys
import os
import pytest

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')


@pytest.fixture
def test_lists():
    """Fixture for linked list tests."""
    from src.linked_list import LinkedList
    empty = LinkedList()
    one = LinkedList(5)
    multi = LinkedList([1, 2, 3, 4, 5])
    return empty, one, multi


def test_node_has_data():
    """Test node object has data."""
    from src.linked_list import Node
    ll = Node(5)
    assert ll.data is 5 and ll.next is None


def test_push_adds_to_the_head(test_lists):
    """Test push, adds to the head of the list."""
    ll = test_lists[1]
    assert ll.head.data is 5


def test_ll_has_head(test_lists):
    """Test ll with iterable has a head."""
    ll = test_lists[2]
    assert ll.head.data is 5


def test_empty_ll_head_none(test_lists):
    """Test empty ll has a head of None."""
    assert test_lists[0].head is None


def test_size_one(test_lists):
    """Test ll of one has length of one."""
    assert test_lists[1]._length is 1


def test_length_multi(test_lists):
    """Test ll of multi has length."""
    assert test_lists[2]._length is 5


def test_empty_list_length(test_lists):
    """Test empty list has no length."""
    assert test_lists[0]._length is 0


def test_when_push_increases_length(test_lists):
    """Test push increases length."""
    ll = test_lists[1]
    length = ll._length
    ll.push(3)
    assert ll._length is length + 1


def test_pop_multi_list(test_lists):
    """Test pop on list of 5."""
    ll = test_lists[2]
    ll.pop()
    assert ll.head.data is 4


def test_pop_returns_data(test_lists):
    """Test pop method returns data of removed node."""
    returned = test_lists[2].pop()
    assert returned is 5


def test_pop_decreases_length(test_lists):
    """Test pop decreases length."""
    ll = test_lists[2]
    length = ll._length
    ll.pop()
    assert ll._length is length - 1


def test_pop_list_one(test_lists):
    """Test pop on list of one."""
    test_lists[1].pop()
    assert test_lists[1].head is None


def test_pop_decreases_length_to_zero(test_lists):
    """Test pop decreases length."""
    ll = test_lists[1]
    length = ll._length
    ll.pop()
    assert ll._length is length - 1


def test_cant_pop_on_empty_list(test_lists):
    """Test pop on an empty list raises error."""
    with pytest.raises(IndexError, message='Cannot pop from an empty list'):
        test_lists[0].pop()
