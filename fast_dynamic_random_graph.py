import numpy as np
from scipy import sparse
from tqdm import tqdm
import time
import sparse
from sparse import COO

def fast_dynamic_er_random_graph(n, steps, up_rate, down_rate, seed=42, directed=False):
    """Returns a $G_{n,mu, lambda}$ dynamic random graph, also known as an dynamic Erdős-Rényi graph.
        The $G_{n,\mu, \lambda}$ model chooses to create inexist edges with probabilty $\mu$ (also known as up-rate)
          and remove exist edges with probability $\lambda$  (also known as doen-rate).
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
        directed : bool, optional (default=False)
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

    if directed:
        adj_t = np.zeros((n, n))
        return adj_t  # TODO: fix for directed
    else:
        adj_t = np.zeros((n, n))

    # $A_{t+1} = (A_t \cdot R_d) + (1-A_t) \cdot R_u)
    # S.t. A_t is the adj matrix, R_d is a binary random matrix with prob of down-rate of non-zero values.
    # R_u is a binary random matrix with prob of up-rate of non-zero values
    compressed_adj_list = [COO.from_numpy(adj_t)]
    for _ in tqdm(range(steps)):
        down_rate_mask = np.random.choice([0, 1], size=(n, n), p=[1 - down_rate, down_rate])
        up_rate_mask = np.random.choice([0, 1], size=(n, n), p=[1 - up_rate, up_rate])

        old_edges_survived = adj_t * down_rate_mask
        new_edges_created = (1 - adj_t) * up_rate_mask

        adj_t = old_edges_survived + new_edges_created

        compressed_adj_t = COO.from_numpy(adj_t)
        compressed_adj_list.append(compressed_adj_t)
    return sparse.stack(compressed_adj_list)


if __name__ == "__main__":
    start_time = time.time()
    n = 1000
    t = 10000
    up_rate = 1 / n
    down_rate = 0.4
    G = fast_dynamic_er_random_graph(n, t, up_rate, down_rate)

    print("--- %s seconds ---" % (time.time() - start_time))
