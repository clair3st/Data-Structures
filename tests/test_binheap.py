"""Testing binary Heap."""

import pytest


@pytest.fixture
def empty_heap():
    """Fixture for empty_heap."""
    from src.binheap import Binheap
    bh = Binheap()
    return bh


def test_push_val_to_head(empty_heap):
    """Test push first val adds to the head."""
    empty_heap.push(3)
    assert empty_heap.container == [None, 3]


def test_push_val(empty_heap):
    """Test push second val adds to the tree."""
    empty_heap.push(3)
    empty_heap.push(2)
    assert empty_heap.container == [None, 3, 2]


def test_push_val_large(empty_heap):
    """Test push val for larger number."""
    empty_heap.push(3)
    empty_heap.push(2)
    empty_heap.push(1)
    empty_heap.push(16)
    assert empty_heap.container == [None, 16, 3, 1, 2]
