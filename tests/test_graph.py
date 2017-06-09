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
    assert sorted(test_graph[2].edges()) == ['B', 'C']


def test_edges_empty(test_graph):
    """Test edges method for empty."""
    assert test_graph[0].edges() == []


def test_remove_edge_full(test_graph):
    """Test remove edge full graph."""
    test_graph[2].add_edge('A', 'B')
    test_graph[2].del_edge('A', 'B')
    assert test_graph[2].edges() == []


def test_remove_edge_empty(test_graph):
    """Test remove edge empty graph."""
    with pytest.raises(KeyError):
        test_graph[0].del_edge('A', 'B')


def test_has_node_true(test_graph):
    """Test has node true."""
    assert test_graph[2].has_node('A')


def test_has_node_false(test_graph):
    """Test has node false."""
    assert not test_graph[0].has_node('A')


def test_has_neighbors_true(test_graph):
    """Test neighbors when exist."""
    test_graph[2].add_edge('A', 'B')
    assert test_graph[2].neighbors('A') == set(['B'])


def test_has_neighbors_false(test_graph):
    """Test neighbors when there are none."""
    assert test_graph[2].neighbors('A') == set()


def test_adjacent_true(test_graph):
    """Test has node true."""
    test_graph[2].add_edge('A', 'B')
    assert test_graph[2].adjacent('A', 'B')


def test_adjacent_false(test_graph):
    """Test ajacent false."""
    assert not test_graph[2].adjacent('A', 'B')


def test_adjacent_error(test_graph):
    """Test adjacent for error."""
    with pytest.raises(KeyError):
        test_graph[0].adjacent('A', 'B')


def test_graph_del_node_empty(test_graph):
    """Test graph del node when node isn't there."""
    with pytest.raises(KeyError):
        test_graph[0].del_node('A')


def test_graph_del_node_no_edges(test_graph):
    """Test graph del node when node no edges."""
    test_graph[1].del_node('A')
    assert test_graph[1].graph == {}


def test_graph_del_node_with_edges(test_graph):
    """Test graph del node with edges."""
    test_graph[2].add_edge('A', 'C')
    test_graph[2].add_edge('B', 'C')
    test_graph[2].add_edge('B', 'C')
    test_graph[2].add_edge('A', 'D')
    test_graph[2].del_node('C')
    assert sorted(test_graph[2].nodes()) == ['A', 'B', 'D', 'E']
    assert sorted(test_graph[2].edges()) == ['D']
