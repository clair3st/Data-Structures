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

    def __init__(self, data=None):
        """Initialize graph."""
        self.graph = {}
        if data:
            for i in data:
                self.add_node(i)

    def nodes(self):
        """Return a list of all nodes in the graph."""
        return list(self.graph.keys())

    def edges(self):
        """Return a list of all edges in the graph."""
        return [edge for edges in self.graph.values() for edge in edges]

    def add_node(self, n):
        """Add a new node to the graph."""
        self.graph.setdefault(n, set())

    def add_edge(self, n1, n2):
        """Add new edge to the graph."""
        self.graph.setdefault(n1, set([n2]))
        self.graph.setdefault(n2, set())
        self.graph[n1].add(n2)

    def del_node(self, n):
        """Delete the node 'n' from the graph."""
        del self.graph[n]
        for k in self.graph:
            self.graph[k].discard(n)

    def del_edge(self, n1, n2):
        """Delete the edge connecting n1 and n2."""
        self.graph[n1].remove(n2)

    def has_node(self, n):
        """Return boolean if 'n' is in the graph."""
        return n in self.graph

    def neighbors(self, n):
        """Return the list of all nodes connected to n by edges."""
        return self.graph[n]

    def adjacent(self, n1, n2):
        """Return boolean if there is an edge connecting n1 and n2."""
        return n2 in self.neighbors(n1)
