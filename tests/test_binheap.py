"""Testing binary Heap."""

import pytest


@pytest.fixture
def heap():
    """Fixture for heap."""
    from src.binheap import Binheap
    bh = Binheap()
    return bh


def test_push_val_to_head(heap):
    """Test push first val adds to the head."""
    heap.push(3)
    assert heap.container == [None, 3]


def test_push_val_to_left(heap):
    """Test push second val adds to the tree."""
    heap.push(3)
    heap.push(2)
    assert heap.container == [None, 3, 2]

