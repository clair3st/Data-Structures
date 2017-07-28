"""Testing module for queue data structure."""

import pytest


@pytest.fixture
def test_queues():
    """Fixture for queue tests."""
    from src.a_queue import Queue
    zero = Queue()
    one = Queue(3)
    multi = Queue([1, 2, 3, 4, 5])
    return zero, one, multi


def test_enque_adds_data(test_queues):
    """Test enque adds data to the tail."""
    test_queues[0].enqueue(3)
    assert test_queues[0]._container.tail.data is 3


def test_enqueue_adds_data_to_tail(test_queues):
    """Test enqueue adds to the tail."""
    test_queues[1].enqueue(2)
    assert test_queues[1]._container.tail.data is 2


def test_enqueue_adds_data_to_tail_and_points_to_prev(test_queues):
    """Test enqueue adds to the tail and point to prev tail."""
    test_queues[1].enqueue(2)
    assert test_queues[1]._container.tail.prev.data is 3


def test_enque_adds_to_size(test_queues):
    """Test enqueue adds size."""
    test_queues[2].enqueue(6)
    assert test_queues[2]._container._length is 6


def test_dequeue_removes_data(test_queues):
    """Test dequeue removes data."""
    test_queues[1].dequeue()
    assert test_queues[1]._container.head is None


def test_removes_data_from_head_and_updates_pointer(test_queues):
    """Test deque updates pointers."""
    test_queues[2].dequeue()
    assert test_queues[1]._container.head.data is 3


def test_deque_removes_from_size(test_queues):
    """Test enqueue adds size."""
    test_queues[2].dequeue()
    assert test_queues[2]._container._length is 4


def test_peek_returns_head(test_queues):
    """Test peek returns head of list."""
    assert test_queues[2].peek() is 5


def test_peek_on_empty(test_queues):
    """Test peek returns None when empty."""
    assert test_queues[0].peek() is None


def test_dequeue_to_get_entire_queue(test_queues):
    """Test successive dequeues returns the queue."""
    q = []
    while test_queues[2]._container._length > 0:
        q.append(test_queues[2].dequeue())
    assert q == [5, 4, 3, 2, 1]


def test_dequeue_on_empty_list(test_queues):
    """Test dequeue on an empty list."""
    with pytest.raises(IndexError):
        test_queues[0].dequeue()


def test_size_on_empty_queue(test_queues):
    """Test size method on empty."""
    assert test_queues[0].size() is 0


def test_size_on_queue_of_one(test_queues):
    """Test size method on a queue of one."""
    assert test_queues[1].size() is 1


def test_size_on_longer_queue(test_queues):
    """Test size method on empty."""
    assert test_queues[2].size() is 5
