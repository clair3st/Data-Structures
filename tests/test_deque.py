"""Test deque implementation."""


import pytest


@pytest.fixture
def test_deque():
    """Deque fixtures."""
    from src.deque import Deque
    empty = Deque()
    one = Deque(3)
    multi = Deque([1, 2, 3, 4, 5])
    return empty, one, multi


def test_init_deque_has_data(test_deque):
    """Test deque has data."""
    assert test_deque[2]._container


def test_init_deque_has_head(test_deque):
    """Test deque has head."""
    assert test_deque[2]._container.head.data is 5


def test_init_deque_has_tail(test_deque):
    """Test deque has tail."""
    assert test_deque[2]._container.tail.data is 1


def test_append_adds_data(test_deque):
    """Test append adds data to the tail."""
    test_deque[0].append(3)
    assert test_deque[0]._container.tail.data is 3


def test_append_adds_data_to_tail(test_deque):
    """Test append adds to the tail."""
    test_deque[1].append(2)
    assert test_deque[1]._container.tail.data is 2


def test_append_adds_data_to_tail_and_points_to_prev(test_deque):
    """Test append adds to the tail and point to prev tail."""
    test_deque[1].append(2)
    assert test_deque[1]._container.tail.prev.data is 3


def test_enque_adds_to_size(test_deque):
    """Test append adds size."""
    test_deque[2].append(6)
    assert test_deque[2]._container._length is 6


def test_appendleft_increases_length(test_deque):
    """Test appendleft increases length."""
    test_deque[0].appendleft(2)
    assert test_deque[0]._container._length is 1


def test_appendleft_updates_head(test_deque):
    """Test appendleft updates head."""
    test_deque[1].appendleft(6)
    assert test_deque[1]._container.head.data is 6


def test_appendleft_points_back(test_deque):
    """Test old head points to new with prev after a appendleft."""
    old_head = test_deque[1]._container.head
    test_deque[1].appendleft(6)
    assert test_deque[1]._container.head is old_head.prev


def test_pop_reduces_length(test_deque):
    """Test pop reduces lists."""
    old_length = test_deque[2]._container._length
    test_deque[2].pop()
    assert test_deque[2]._container._length is old_length - 1


def test_pop_removes_tail(test_deque):
    """Test pop removes tail."""
    new_tail = test_deque[2]._container.tail.prev.data
    test_deque[2].pop()
    assert test_deque[2]._container.tail.data is new_tail


def test_pop_removes_next_pointer(test_deque):
    """Test pop changes prev pointer."""
    test_deque[2].pop()
    assert test_deque[2]._container.tail.next is None


def test_pop_list_one(test_deque):
    """Test pop decreases length."""
    test_deque[1].pop()
    assert test_deque[1]._container._length is 0


def test_cant_pop_on_empty_list(test_deque):
    """Test pop on an empty list raises error."""
    with pytest.raises(IndexError, message='Cannot pop from an empty list'):
        test_deque[0].pop()


def test_pop_sequence(test_deque):
    """Test that entire sequence is returned by successive pops."""
    l = []
    while True:
        try:
            poped_data = test_deque[2].pop()
            l.append(poped_data)
        except IndexError:
            break
    assert l == [1, 2, 3, 4, 5]


def test_pop_append(test_deque):
    """Append data and pop it off."""
    test_deque[1].append(9)
    poped_data = test_deque[1].pop()
    assert poped_data is 9


def test_popleft_reduces_length(test_deque):
    """Test popleft reduces lists."""
    old_length = test_deque[2]._container._length
    test_deque[2].popleft()
    assert test_deque[2]._container._length is old_length - 1


def test_popleft_removes_tail(test_deque):
    """Test popleft removes head."""
    new_head = test_deque[2]._container.head.next.data
    test_deque[2].popleft()
    assert test_deque[2]._container.head.data is new_head


def test_popleft_removes_next_pointer(test_deque):
    """Test popleft changes prev pointer."""
    test_deque[2].popleft()
    assert test_deque[2]._container.head.prev is None


def test_popleft_list_one(test_deque):
    """Test popleft decreases length."""
    test_deque[1].popleft()
    assert test_deque[1]._container._length is 0


def test_cant_popleft_on_empty_list(test_deque):
    """Test popleft on an empty list raises error."""
    with pytest.raises(
            IndexError, message='Cannot popleft from an empty list'
    ):
        test_deque[0].popleft()


def test_popleft_sequence(test_deque):
    """Test that entire sequence is returned by successive poplefts."""
    l = []
    while True:
        try:
            poplefted_data = test_deque[2].popleft()
            l.append(poplefted_data)
        except IndexError:
            break
    assert l == [5, 4, 3, 2, 1]


def test_popleft_appendleft(test_deque):
    """Append data and popleft it off."""
    test_deque[1].appendleft(9)
    poplefted_data = test_deque[1].popleft()
    assert poplefted_data is 9


def test_size_method_append(test_deque):
    """Append and test size."""
    test_deque[0].append(2)
    assert test_deque[0].size() == 1


def test_size_method_appendleft(test_deque):
    """Appendleft and test size."""
    test_deque[0].appendleft(2)
    assert test_deque[0].size() == 1


def test_size_method_pop(test_deque):
    """Pop and test size."""
    test_deque[1].pop()
    assert test_deque[0].size() == 0


def test_size_method_popleft(test_deque):
    """Pop and test size."""
    test_deque[1].popleft()
    assert test_deque[0].size() == 0


def test_peek(test_deque):
    """Test peek method."""
    peek = test_deque[2].peek()
    assert peek == test_deque[2]._container.head.data


def test_peek_size(test_deque):
    """Test peek method does not change size."""
    size = test_deque[2].size()
    test_deque[2].peek()
    assert size == test_deque[2].size()


def test_peek_empty(test_deque):
    """Test peek method."""
    peek = test_deque[0].peek()
    assert peek is None


def test_peekleft(test_deque):
    """Test peekleft method."""
    peekleft = test_deque[2].peekleft()
    assert peekleft == test_deque[2]._container.tail.data


def test_peekleft_size(test_deque):
    """Test peekleft method does not change size."""
    size = test_deque[2].size()
    test_deque[2].peekleft()
    assert size == test_deque[2].size()


def test_peekleft_empty(test_deque):
    """Test peekleft method."""
    peekleft = test_deque[0].peekleft()
    assert peekleft is None
