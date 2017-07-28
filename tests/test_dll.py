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


def test_pop_returns_data(test_lists):
    """Test pop returns data."""
    assert test_lists[2].pop() is 5


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
    assert test_lists[1].tail is old_tail.next


def test_append_on_empty_list(test_lists):
    """Test append updates tail."""
    test_lists[0].append(6)
    assert test_lists[0].tail.data is 6
    assert test_lists[0].head.data is 6


def test_append_next_pointer_is_none(test_lists):
    """Test append next pointer is none."""
    test_lists[2].append(6)
    assert test_lists[2].tail.next is None


def test_pop_sequence(test_lists):
    """Test that entire sequence is returned by successive pops."""
    l = []
    while True:
        try:
            popped_data = test_lists[2].pop()
            l.append(popped_data)
        except IndexError:
            break
    assert l == [5, 4, 3, 2, 1]


def test_push_pop(test_lists):
    """Push data and pop it off."""
    test_lists[1].push(9)
    popped_data = test_lists[1].pop()
    assert popped_data is 9


def test_shift_reduces_length(test_lists):
    """Test shift reduces lists."""
    old_length = test_lists[2]._length
    test_lists[2].shift()
    assert test_lists[2]._length is old_length - 1


def test_shift_removes_tail(test_lists):
    """Test shift removes tail."""
    new_tail = test_lists[2].tail.prev.data
    test_lists[2].shift()
    assert test_lists[2].tail.data is new_tail


def test_shift_removes_next_pointer(test_lists):
    """Test shift changes prev pointer."""
    test_lists[2].shift()
    assert test_lists[2].tail.next is None


def test_shift_list_one(test_lists):
    """Test shift decreases length."""
    test_lists[1].shift()
    assert test_lists[1]._length is 0


def test_cant_shift_on_empty_list(test_lists):
    """Test shift on an empty list raises error."""
    with pytest.raises(IndexError, message='Cannot shift from an empty list'):
        test_lists[0].shift()


def test_shift_sequence(test_lists):
    """Test that entire sequence is returned by successive shifts."""
    l = []
    while True:
        try:
            shifted_data = test_lists[2].shift()
            l.append(shifted_data)
        except IndexError:
            break
    assert l == [1, 2, 3, 4, 5]


def test_shift_append(test_lists):
    """Append data and shift it off."""
    test_lists[1].append(9)
    shifted_data = test_lists[1].shift()
    assert shifted_data is 9


def test_remove_middle_of_list(test_lists):
    """Test remove from middle of list."""
    test_lists[2].remove(3)
    assert test_lists[2]._repr() == [5, 4, 2, 1]


def test_remove_head_of_list(test_lists):
    """Test remove from head of list."""
    test_lists[2].remove(5)
    assert test_lists[2]._repr() == [4, 3, 2, 1]


def test_remove_tail_of_list(test_lists):
    """Test remove from tail of list."""
    test_lists[2].remove(1)
    assert test_lists[2]._repr() == [5, 4, 3, 2]


def test_remove_middle_decreases_length(test_lists):
    """Test remove from middle of list decreases length."""
    test_lists[2].remove(3)
    assert test_lists[2]._length is 4


def test_remove_head_decreases_length(test_lists):
    """Test remove from head of list decreases length."""
    test_lists[2].remove(5)
    assert test_lists[2]._length is 4


def test_remove_tail_decreases_length(test_lists):
    """Test remove from tail of list decreases length."""
    test_lists[2].remove(1)
    assert test_lists[2]._length is 4


def test_remove_middle_updates_pointers(test_lists):
    """Test remove from middle of list updates pointers."""
    test_lists[2].remove(3)
    assert test_lists[2].head.next.next.data is 2


def test_remove_head_pointers(test_lists):
    """Test remove from head of list changes pointers."""
    test_lists[2].remove(5)
    assert test_lists[2].head.data is 4
    assert test_lists[2].head.prev is None


def test_remove_tail_pointers(test_lists):
    """Test remove from tail of list changes pointers."""
    test_lists[2].remove(1)
    assert test_lists[2].tail.data is 2
    assert test_lists[2].tail.next is None


def test_remove_list_of_one_length(test_lists):
    """Test remove on list of one."""
    test_lists[1].remove(3)
    assert test_lists[1]._length is 0


def test_remove_list_of_one(test_lists):
    """Test remove on list of one."""
    test_lists[1].remove(3)
    assert test_lists[1].head is None
    assert test_lists[1].tail is None


def test_remove_list_of_none(test_lists):
    """Test remove on list of none."""
    with pytest.raises(ValueError):
        test_lists[0].remove(3)


def test_remove_of_list_false(test_lists):
    """Test remove from middle of list."""
    with pytest.raises(ValueError):
        test_lists[2].remove(9)
