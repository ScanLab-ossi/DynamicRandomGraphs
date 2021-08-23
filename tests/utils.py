def get_number_of_potential_edges(nodes: int, is_directed: bool):
    if is_directed:
        return nodes * (nodes - 1) / 2
    else:
        return nodes * (nodes - 1)


def get_expected_er_model_density(alpha: float, beta: float):
    return alpha / (alpha + beta)
