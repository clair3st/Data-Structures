"""Test module for graph."""

import pytest


@pytest.fixture
def test_graph():
    """Fixture for graph."""
    from src.graph import Graph
    g = Graph(['A', 'B', 'C', 'D', 'E'])
    g1 = Graph(['A'])
    g0 = Graph()
    return g0, g1, g


def test_nodes_empty(test_graph):
    """Test nodes method list."""
    assert test_graph[0].nodes() == []


def test_nodes_one(test_graph):
    """Test nodes method list."""
    assert test_graph[1].nodes() == ['A']


def test_nodes_graph(test_graph):
    """Test nodes method list."""
    assert sorted(test_graph[2].nodes()) == ['A', 'B', 'C', 'D', 'E']
