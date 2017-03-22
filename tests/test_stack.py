"""Test for Stack implementation."""

import pytest


@pytest.fixture
def test_stack():
    """Fixture for testing."""
    from src.stack import Stack
    empty = Stack()
    one = Stack(5)
    multi = Stack([1, 2, 'three', 4, 5])
    return empty, one, multi


def test_stack_is_initialized(test_stack):
    """Test stack."""
    assert test_stack[0]._stack._length is 0


def test_empty_stack_push(test_stack):
    """Test can push on an empty stack."""
    test_stack[0].push(3)
    assert test_stack[0]._stack._length is 1


def test_stack_of_one_push(test_stack):
    """Test can push on an stack of 1."""
    test_stack[1].push(2)
    assert test_stack[1]._stack.head.data is 2


def test_stack_of_multiple_push(test_stack):
    """Test can push on an stack of multiple."""
    test_stack[2].push(2)
    assert test_stack[2]._stack.head.data is 2
