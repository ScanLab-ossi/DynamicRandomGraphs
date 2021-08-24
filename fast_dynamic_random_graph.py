import numpy as np
from tqdm import tqdm
from sparse import COO
import pandas as pd
from pathlib import Path
import time


def adj_matrix_to_df(adj_t, step=None):
    row, col = np.where(adj_t)
    coo = np.rec.fromarrays([row, col], names='source destination'.split())
    df = pd.DataFrame.from_records(coo, columns=['source', 'destination'])
    if step is not None:
        df['datetime'] = step
        df = df[['datetime', 'source', 'destination']]
    return df


def get_binary_matrix_mask(n: int, rate_to_one: float):
    return np.random.choice([0, 1], size=(n, n), p=[1 - rate_to_one, rate_to_one])


def fast_dynamic_er_random_graph(n, steps, up_rate, down_rate, seed=None, write_to_csv=False, is_directed=False,
                                 output_file_name=None):
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
        write_to_csv: bool, optional (default=False)
            False will return pandas dataframe, True will write the results to CSV (preferred for huge networks)
        output_file_name : str
            Destination for csv file, relevant only if ''write_to_csv'' is True
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
    if write_to_csv is True and output_file_name is None:
        output_file_name = Path(
            'data') / f'random_undirected_er_{n}_nodes_{steps}_steps_{up_rate}_up_{down_rate}_down_{time.time()}.csv'

    # Init t=0 adjacency matrix
    adj_t = np.zeros((n, n))

    # $A_{t+1} = (A_t \cdot (1-R_d)) + (1-A_t) \cdot R_u)$
    # S.t. A_t is the adj matrix, R_d is a binary random matrix with prob of down-rate of non-zero values.
    # R_u is a binary random matrix with prob of up-rate of non-zero values
    df_adj = pd.DataFrame(columns=[['datetime', 'source', 'destination']])
    for step in tqdm(range(steps)):
        down_rate_mask = get_binary_matrix_mask(n, down_rate)
        up_rate_mask = get_binary_matrix_mask(n, up_rate)

        old_edges_survived = adj_t * (1 - down_rate_mask)
        new_edges_created = (1 - adj_t) * up_rate_mask

        adj_t = old_edges_survived + new_edges_created
        # np.fill_diagonal(adj_t, 0)  # remove self-edges
        if is_directed:
            df_compressed_adj_t = adj_matrix_to_df(adj_t, step)
        else:  # make the adj matrix symmetric again
            df_compressed_adj_t = adj_matrix_to_df(np.tril(adj_t), step)

        if df_adj.size == 0:
            df_adj = df_compressed_adj_t.copy()
        else:
            df_adj = pd.concat([df_adj, df_compressed_adj_t])

        if write_to_csv:
            if df_adj.size > 100000:
                if output_file_name.is_file():
                    df_adj.to_csv(output_file_name, mode='a', header=False, index=False)
                else:
                    df_adj.to_csv(output_file_name, mode='a', header=True, index=False)

                df_adj = pd.DataFrame(columns=[['datetime', 'source', 'destination']])

    if write_to_csv:
        df_adj.to_csv(output_file_name, mode='a', header=False, index=False)

    if not write_to_csv:
        return df_adj

    else:
        return
