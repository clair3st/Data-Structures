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


def test_size_function(test_lists):
    """Test size on empty list."""
    assert test_lists[0].size() is 0


def test_size_function_list(test_lists):
    """Test size on multi list."""
    assert test_lists[2].size() is 5


def test_size_after_push(test_lists):
    """Test size after push."""
    ll = test_lists[0]
    length = ll.size()
    ll.push(4)
    assert ll.size() is length + 1


def test_size_after_pop(test_lists):
    """Test size after pop."""
    ll = test_lists[2]
    length = ll.size()
    ll.pop()
    assert ll.size() is length - 1


def test_size_after_push_and_pop(test_lists):
    """Test size after push and pop."""
    ll = test_lists[2]
    ll.push(4)
    ll.push(2)
    ll.pop()
    assert ll.size() is 6


def test_search_on_list(test_lists):
    """Test search returns node."""
    assert test_lists[2].search(2).data is 2


def test_search_on_list_no_value(test_lists):
    """Test search for a list with no val."""
    assert test_lists[2].search(9) is None


def test_remove_on_list(test_lists):
    """Test remove work for node in list."""
    test_lists[2].remove(4)
    assert test_lists[2].size() is 4


def test_remove_second_end_of_list(test_lists):
    """Test remove node second last in list."""
    test_lists[2].remove(2)
    assert test_lists[2].size() is 4


def test_remove_on_end_of_list(test_lists):
    """Test remove node last in list."""
    test_lists[2].remove(1)
    assert test_lists[2].size() is 4


def test_remove_on_list_with_no_node(test_lists):
    """Test remove node that isnt in list."""
    test_lists[2].remove(9)
    assert test_lists[2].size() is 5


def test_remove_on_empty_list(test_lists):
    """Test remove from empty list."""
    test_lists[0].remove(1)
    assert test_lists[0].size() is 0


def test_remove_on_list_one_list(test_lists):
    """Test remove from list of 1."""
    test_lists[1].remove(5)
    assert test_lists[1].size() is 0


def test_remove_on_start_of_list(test_lists):
    """Test remove start node in list."""
    test_lists[2].remove(5)
    assert test_lists[2].size() is 4


def test_display_method(test_lists):
    """Test display method."""
    assert test_lists[2].display() == '(5, 4, 3, 2, 1)'


def test_display_method_one(test_lists):
    """Test display method."""
    assert test_lists[1].display() == '(5)'
