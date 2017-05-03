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
    assert test_deque[2].data


def test_init_deque_has_head(test_deque):
    """Test deque has head."""
    assert test_deque[2].head.data is 5


def test_init_deque_has_tail(test_deque):
    """Test deque has tail."""
    assert test_deque[2].tail.data is 1
