"""Python implementation of a Graph Data structure."""


class Graph(object):
    """
    Graph implementation.

    Graph data structure supports following methods:

    nodes(): return a list of all nodes in the graph.
    edges(): return a list of all edges in the graph.
    add_node(n): adds a new node 'n' to the graph.
    add_edge(n1, n2): adds a new edge to the graph connecting 'n1' and 'n2', if
    either n1 or n2 are not already present in the graph, they should be added.
    del_node(n): deletes the node 'n' from the graph, raises an error if no
    such node exists.
    del_edge(n1, n2): deletes the edge connecting 'n1' and 'n2' from the graph,
    raises an error if no such edge exists.
    has_node(n): True if node 'n' is contained in the graph, False if not.
    neighbors(n): returns the list of all nodes connected to 'n' by edges,
    raises an error if n is not in g.
    adjacent(n1, n2): returns True if there is an edge connecting n1 and n2,
    False if not, raises an error if either of the supplied nodes are not in g.
    """

    def __init__(self):
        """Initialize graph."""
        self.graph = {}

    def nodes(self):
        """Return a list of all nodes in the graph."""
        pass

    def edges(self):
        """Return a list of all edges in the graph."""
        pass

    def add_node(self, n):
        """Add a new node to the graph."""
        pass

    def add_edge(self, n1, n2):
        """Add new edge to the graph."""
        pass

    def del_edge(self, n1, n2):
        """Delete the edge connecting n1 and n2."""
        pass

    def has_node(self, n):
        """Return boolean if 'n' is in the graph."""
        pass

    def neighbors(self, n):
        """Return the list of all nodes connected to n by edges."""
        pass

    def adjacent(self, n1, n2):
        """Return boolean if there is an edge connecting n1 and n2."""
        pass
