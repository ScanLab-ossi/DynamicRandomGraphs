import dynetx as dn
import networkx as nx
import itertools
from random import random


def get_edges_iterator(n: int, directed=False):
    if directed:
        edges = itertools.permutations(range(n), 2)
    else:
        edges = itertools.combinations(range(n), 2)
    return edges


def dynamic_er_random_graph(n, steps, up_rate, down_rate, seed=None, is_directed=False):
    """Returns a $G_{n,mu, lambda}$ dynamic random graph, also known as an dynamic Erdős-Rényi graph.
    The $G_{n,\mu, \lambda}$ model chooses to create inexist edges with probabilty $\mu$ (also known as up-rate)
      and remove exist edges with probability $\lambda$  (also known as down-rate).
    Parameters
    ----------
    n : int
        The number of nodes.
    steps: int
        The number of timestamps in the temporal network. The length of the network in the time axis.
    up_rate : float
        Probability for edge creation.
    down_rate: float
        Probability of edge removal
    seed : integer, random_state, or None (default)
        Indicator of random number generation state.
        See :ref:`Randomness<randomness>`.
    is_directed : bool, optional (default=False)
        If True, this function returns a directed graph.
    See Also
    --------
    gnp_random_graph
    fast_gnp_random_graph

    Notes
    -----
    This algorithm runs in $O(?)$ time.

    References
    ----------
    .. [1] Mandjes, M., Starreveld, N., Bekker, R., & Spreij, P. (2019). Dynamic Erdős-Rényi Graphs.
                In Computing and Software Science (pp. 123-140). Springer, Cham.‏.
    """

    if is_directed:
        G = nx.DiGraph()
        dynamic_graph = dn.DynDiGraph()
    else:
        G = nx.Graph()
        dynamic_graph = dn.DynGraph()

    edges = list(get_edges_iterator(n, is_directed))
    # Init graph nodes
    G.add_nodes_from(range(n))
    dynamic_graph.add_nodes_from(range(n))

    list_of_graph_snapshots = list()

    # When t=0:
    if up_rate <= 0:
        list_of_graph_snapshots = [G] * steps

    elif up_rate >= 1:
        G.add_edges_from(edges)
        list_of_graph_snapshots = [G] * steps

    else:  # up-rate is in between (0,1)
        for e in edges:
            if random() < up_rate:
                G.add_edge(*e)
        list_of_graph_snapshots.append(G)

        for t in range(1, steps):
            G_t = nx.Graph()
            edges = get_edges_iterator(n, is_directed)

            for e in edges:
                if list_of_graph_snapshots[t - 1].has_edge(*e):  # check if edge is in graph in previous step
                    if random() > down_rate:
                        G_t.add_edge(*e)
                else:  # un-exist edge
                    if random() < up_rate:
                        G_t.add_edge(*e)
            list_of_graph_snapshots.append(G_t)

    for t, graph in enumerate(list_of_graph_snapshots):
        dynamic_graph.add_interactions_from(graph.edges(data=True), t=t)

    return dynamic_graph
