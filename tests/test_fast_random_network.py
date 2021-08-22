import random_dynamic_graph.fast_dynamic_random_graph as fdrg
import numpy as np
import pandas as pd
from pandas._testing import assert_frame_equal


def test_adj_matrix_to_df_zeros_matrix():
    s = np.zeros((10, 10))
    test_df = fdrg.adj_matrix_to_df(adj_t=s, step=1)
    expected_df = pd.DataFrame(columns=['datetime', 'source', 'destination'])
    assert_frame_equal(test_df, expected_df, check_dtype=False, check_index_type=False)


def test_adj_matrix_to_df_not_empty_matrix():
    s = np.zeros((10, 10))
    s[0, 1] = 1
    test_df = fdrg.adj_matrix_to_df(adj_t=s, step=1)

    data = {'datetime': [1], 'source': [0], 'destination': [1]}
    expected_df = pd.DataFrame.from_dict(data)
    assert_frame_equal(test_df, expected_df, check_dtype=False, check_index_type=False)
