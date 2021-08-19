import pytest
import dynamic_random_graphs as drg
import dynetx as dn


def test_get_edges_iterator_directed():
    edges = drg.get_edges_iterator(3, directed=True)
    assert list(edges) == [(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)]


def test_get_edges_iterator_undirected():
    edges = drg.get_edges_iterator(3, directed=False)
    assert list(edges) == [(0, 1), (0, 2), (1, 2)]


def test_create_full_graph_directed():
    G_ref = dn.DynDiGraph()
    G_ref.add_nodes_from(range(3))
    for t in range(5):
        G_ref.add_interactions_from([(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)], t=t)

    G = drg.dynamic_er_random_graph(3, 5, 1, 0.8, None, True)
    assert G.order() == G_ref.order() == 3  # number of nodes
    for i in range(5):  # number of edges per t
        assert (dn.number_of_interactions(G, t=i) == dn.number_of_interactions(G_ref, t=0) == 6)


def test_create_full_graph_undirected():
    G_ref = dn.DynDiGraph()
    G_ref.add_nodes_from(range(3))
    for t in range(5):
        G_ref.add_interactions_from([(0, 1), (0, 2), (1, 2)], t=t)

    G = drg.dynamic_er_random_graph(3, 5, 1, 0.8, None, False)
    assert G.order() == G_ref.order() == 3  # number of nodes
    for i in range(5):  # number of edges per t
        assert (dn.number_of_interactions(G, t=i) == dn.number_of_interactions(G_ref, t=0) == 3)


test_create_full_graph_directed()
test_create_full_graph_directed()
