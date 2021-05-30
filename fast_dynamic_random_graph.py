import numpy as np
from scipy import sparse
from tqdm import tqdm
import sparse
from sparse import COO
import pandas as pd


def adj_matrix_to_df(adj_t, step=None):
    row, col = np.where(adj_t)
    coo = np.rec.fromarrays([row, col], names='row col'.split())
    df = pd.DataFrame.from_records(coo, columns=['row', 'col'])
    if step is not None:
        df['step'] = step
        df = df[['step', 'row', 'col']]
    return df


def fast_dynamic_er_random_graph(n, steps, up_rate, down_rate, output_file_name, directed=False, ):
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
        output_file_name : str
            Destination for csv file
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

    adj_t = np.zeros((n, n))

    # $A_{t+1} = (A_t \cdot R_d) + (1-A_t) \cdot R_u)
    # S.t. A_t is the adj matrix, R_d is a binary random matrix with prob of down-rate of non-zero values.
    # R_u is a binary random matrix with prob of up-rate of non-zero values
    compressed_adj_list = [COO.from_numpy(adj_t)]
    df_adj = pd.DataFrame(columns=[['step', 'row', 'col']])
    for step in tqdm(range(steps)):
        down_rate_mask = np.random.choice([0, 1], size=(n, n), p=[1 - down_rate, down_rate])
        up_rate_mask = np.random.choice([0, 1], size=(n, n), p=[1 - up_rate, up_rate])

        old_edges_survived = adj_t * down_rate_mask
        new_edges_created = (1 - adj_t) * up_rate_mask

        adj_t = old_edges_survived + new_edges_created
        np.fill_diagonal(adj_t, 0)  # remove self-edges
        if directed:
            #compressed_adj_t = COO.from_numpy(adj_t)
            df_compressed_adj_t = adj_matrix_to_df(adj_t, step)
        else:  # make the adj matrix symmetric again
            #compressed_adj_t = COO.from_numpy(np.tril(adj_t) + np.tril(adj_t, -1).T)
            df_compressed_adj_t = adj_matrix_to_df(np.tril(adj_t), step)

        df_adj = pd.concat([df_adj, df_compressed_adj_t])
        if df_adj.size > 10000:
            df_adj.to_csv(output_file_name, mode='a', header=False, index=False)
            df_adj = pd.DataFrame(columns=[['step', 'row', 'col']])

        #compressed_adj_list.append(compressed_adj_t)

    return #sparse.stack(compressed_adj_list)
