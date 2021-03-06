import random
import statistics
from os import path, write
from typing import Optional

import numpy as np
import pandas as pd
import pytest
import random_graph_generator.fast_dynamic_random_graph as fdrg
import tests.utils as utils
from pandas._testing import assert_frame_equal


def test_adj_matrix_to_df_zeros_matrix():
    s = np.zeros((10, 10))
    test_df = fdrg.adj_matrix_to_df(adj_t=s, step=1)
    expected_df = pd.DataFrame(columns=["datetime", "source", "destination"])
    assert_frame_equal(test_df, expected_df, check_dtype=False, check_index_type=False)


def test_adj_matrix_to_df_not_empty_matrix():
    s = np.zeros((10, 10))
    s[0, 1] = 1
    test_df = fdrg.adj_matrix_to_df(adj_t=s, step=1)

    data = {"datetime": [1], "source": [0], "destination": [1]}
    expected_df = pd.DataFrame.from_dict(data)
    assert_frame_equal(test_df, expected_df, check_dtype=False, check_index_type=False)


def get_delta_between_fast_random_graph_density_and_expected(
    write_to_csv: bool = False,
    is_directed: bool = False,
    output_file_name: Optional[str] = None,
):
    nodes = random.randint(25, 100)
    steps = random.randint(25, 100)
    alpha = random.uniform(0.0001, 0.1)
    beta = random.uniform(0.0001, 0.9999)
    df = fdrg.fast_dynamic_er_random_graph(
        nodes, steps, alpha, beta, write_to_csv, is_directed, output_file_name
    )
    total_edges = len(df.index)
    max_number_edges = utils.get_number_of_potential_edges(nodes, is_directed)
    real_density = total_edges / (max_number_edges * steps)
    expected_density = utils.get_expected_er_model_density(alpha, beta)
    return real_density - expected_density


def get_avg_delta_and_std(iterations: int, is_directed: bool = False):
    delta_list = list()
    for _ in range(iterations):
        delta_list.append(
            get_delta_between_fast_random_graph_density_and_expected(
                write_to_csv=False, is_directed=is_directed
            )
        )
    avg_delta = sum(delta_list) / len(delta_list)
    std_delta = statistics.stdev(delta_list)
    return avg_delta, std_delta


# def test_create_fast_undirected_graph_density():
#     avg_delta, std_delta = get_avg_delta_and_std(iterations=10, is_directed=False)
#     assert avg_delta < 0.1
#     assert std_delta < 0.15


@pytest.mark.slow
def test_create_fast_undirected_graph_density_slow():
    avg_delta, std_delta = get_avg_delta_and_std(iterations=200, is_directed=False)
    assert avg_delta < 0.1
    assert std_delta < 0.15


@pytest.mark.slow
def test_create_fast_directed_graph_density_slow():
    avg_delta, std_delta = get_avg_delta_and_std(iterations=200, is_directed=True)
    assert avg_delta < 0.1
    assert std_delta < 0.15


def test_get_binary_matrix_mask_size():
    arr = fdrg.get_binary_matrix_mask(10, 0.5)
    assert arr.shape == (10, 10)
    arr = fdrg.get_binary_matrix_mask(100, 0.3)
    assert arr.shape == (100, 100)


def test_get_binary_matrix_mask_ones_counter():
    nodes = 100
    x = nodes ** 2
    p = 0.3
    arr = fdrg.get_binary_matrix_mask(nodes, p)
    counter = np.sum(arr)
    expected_count = p * x
    std = np.sqrt(x * p * (1 - p))  # std of binomial distribution
    assert expected_count + std > counter > expected_count - std


def test_create_graph_writing(tmpdir):
    file_ = tmpdir.join("output.csv")
    df = fdrg.fast_dynamic_er_random_graph(
        n=50,
        steps=50,
        up_rate=0.1,
        down_rate=0.5,
        write_to_csv=True,
        is_directed=False,
        output_file_name=file_,
    )
    assert path.exists(file_)
