"""Testing module for priorityq."""

import pytest


@pytest.fixture
def test_q():
    """Test fixtures of priority qs."""
    from src.priorityq import PriorityQ
    q0 = PriorityQ()
    return q0


def test_priority_q_insert(test_q):
    """Test priorityq insert on a list of none."""
    test_q.insert('sgds', 10)
    assert test_q._container.container[1] == (10, 'sgds')
