import pytest
import random_dynamic_graph.dynamic_random_graph as drg
import dynetx as dn
import random
import statistics
import random_dynamic_graph.tests.utils as utils


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


def test_create_empty_graph_directed():
    G = drg.dynamic_er_random_graph(3, 5, 0, 0.5, None, True)
    assert G.order() == 3  # number of nodes
    for i in range(5):  # number of edges per t
        assert (dn.number_of_interactions(G, t=i) == 0)


def test_create_empty_graph_undirected():
    G = drg.dynamic_er_random_graph(3, 5, 0, 0.5, None, False)
    assert G.order() == 3  # number of nodes
    for i in range(5):  # number of edges per t
        assert (dn.number_of_interactions(G, t=i) == 0)


def get_delta_between_nx_random_graph_density_and_expected(is_directed=False):
    nodes = random.randint(25, 50)
    steps = random.randint(25, 50)
    alpha = random.uniform(0.0001, 0.1)
    beta = random.uniform(0.0001, 0.9999)
    G = drg.dynamic_er_random_graph(nodes, steps, alpha, beta, None, False)
    total_edges = sum(dn.number_of_interactions(G, t=i) for i in range(steps))
    max_number_edges = utils.get_number_of_potential_edges(nodes, is_directed)
    real_density = total_edges / (max_number_edges * steps)
    expected_density = utils.get_expected_er_model_density(alpha, beta)
    return real_density - expected_density


def test_create_undirected_graph_density():
    delta_list = list()
    for i in range(10):
        delta = get_delta_between_nx_random_graph_density_and_expected()
        delta_list.append(delta)
    avg_delta = sum(delta_list) / len(delta_list)
    std_delta = (statistics.stdev(delta_list))
    assert avg_delta < 0.1
    assert std_delta < 0.15


@pytest.mark.slow
def test_create_undirected_graph_density_slow():
    delta_list = list()
    for i in range(100):
        delta = get_delta_between_nx_random_graph_density_and_expected()
        delta_list.append(delta)
    avg_delta = sum(delta_list) / len(delta_list)
    std_delta = (statistics.stdev(delta_list))
    assert avg_delta < 0.1
    assert std_delta < 0.15


def test_create_directed_graph_density():
    delta_list = list()
    for i in range(2):
        delta = get_delta_between_nx_random_graph_density_and_expected(is_directed=True)
        delta_list.append(delta)
    avg_delta = sum(delta_list) / len(delta_list)
    std_delta = (statistics.stdev(delta_list))
    assert avg_delta < 0.1
    assert std_delta < 0.15


@pytest.mark.slow
def test_create_directed_graph_density_slow():
    delta_list = list()
    for i in range(100):
        delta = get_delta_between_nx_random_graph_density_and_expected(is_directed=True)
        delta_list.append(delta)
    avg_delta = sum(delta_list) / len(delta_list)
    std_delta = (statistics.stdev(delta_list))
    assert avg_delta < 0.1
    assert std_delta < 0.15
