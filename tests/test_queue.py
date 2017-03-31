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
