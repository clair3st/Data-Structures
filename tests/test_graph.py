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


def test_add_nodes(test_graph):
    """Test add node adds a node."""
    test_graph[0].add_node('A')
    assert test_graph[0].nodes() == ['A']


def test_add_nodes_dont_duplicate(test_graph):
    """Test add node doesn't duplicate."""
    test_graph[1].add_node('A')
    assert test_graph[1].nodes() == ['A']
