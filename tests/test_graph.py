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


def test_add_edge_known_nodes(test_graph):
    """Test add an edge."""
    test_graph[2].add_edge('A', 'B')
    assert test_graph[2].graph['A'] == {'B'}


def test_add_egde_new_nodes(test_graph):
    """Test add an edge with nodes that don't exist."""
    test_graph[0].add_edge('A', 'B')
    assert test_graph[0].graph == {'A': {'B'}, 'B': set()}


def test_edges_full(test_graph):
    """Test edges returned in list with edge method."""
    test_graph[2].add_edge('A', 'B')
    test_graph[2].add_edge('A', 'C')
    assert test_graph[2].edges() == ['B', 'C']


def test_edges_empty(test_graph):
    """Test edges method for empty."""
    assert test_graph[0].edges() == []


def test_remove_edge_full(test_graph):
    """Test remove edge full graph."""
    test_graph[2].add_edge('A', 'B')
    test_graph[2].del_edge('A', 'B')
    assert test_graph[2].edges() == []
