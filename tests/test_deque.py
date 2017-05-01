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
