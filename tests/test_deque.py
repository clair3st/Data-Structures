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
