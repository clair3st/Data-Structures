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
