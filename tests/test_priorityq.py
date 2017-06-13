"""Testing module for priorityq."""

import pytest


@pytest.fixture
def test_q():
    """Test fixtures of priority qs."""
    from src.priorityq import PriorityQ
    q0 = PriorityQ()
    q1 = PriorityQ()
    q1.insert('sgds', 10)
    q1.insert('another', 9)
    q1.insert('another', 8)
    q1.insert('another', 7)
    q1.insert('another', 6)
    return q0, q1


def test_priority_q_insert(test_q):
    """Test priorityq insert on a list of none."""
    test_q[0].insert('sgds', 10)
    assert test_q[0]._container.container[1] == (10, 'sgds')


def test_priority_q_insert_multiple(test_q):
    """Test priorityq insert multi on a list of none."""
    assert test_q[1]._container.container[1] == (10, 'sgds')


def test_priority_q_new_highest(test_q):
    """Test priorityq changes head with new highest priority."""
    test_q[1].insert('highest', 100)
    assert test_q[1]._container.container[1] == (100, 'highest')


def test_priority_q_pop(test_q):
    """Test priority q pop, remove highest priority."""
    assert test_q[1].pop() == 'sgds'


def test_priority_q_pop_empty(test_q):
    """Test priority q pop, raises index error on empty."""
    with pytest.raises(IndexError):
        test_q[0].pop()


def test_peek_returns_highest_priority(test_q):
    """Test priority q returns highest value."""
    assert test_q[1].peek() == 'sgds'


def test_priority_q_peek_empty(test_q):
    """Test priority q peek, returns None."""
    assert test_q[0].peek() is None
