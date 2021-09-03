import itertools
import multiprocessing
import time
from pathlib import Path
import json
from joblib import Parallel, delayed

import fast_dynamic_random_graph as fdrg
import dynamic_random_graph as drg

import argparse

parser = argparse.ArgumentParser(description='Random Network generation')

parser.add_argument('--name', default='random_network', type=str,
                    help='Name of the network.')
parser.add_argument('--out_file', default='random_network',
                    help='path to output network file')
parser.add_argument('--nodes', default=100, type=int,
                    help='Number of nodes')
parser.add_argument('--steps', default=1000, type=int,
                    help='Number of time steps')
parser.add_argument('--is_directed', default=False, type=bool,
                    help='is directed graph (default=False)')
parser.add_argument('--up', default=0.01, type=float,
                    help='up-rate parameter; the probability of an edge to appear at the first time (default=0.01)')
parser.add_argument('--down', default=0.5, type=float,
                    help='down-rate parameter;'
                         ' the probability of an exist edge to disappear at the next time (default=0.5)')
parser.add_argument('--mode', default='pandas', type=str,
                    help='Mode of the network - pandas-based or networkX (default=pandas)')
parser.add_argument('--config', default=None, type=str,
                    help='path of config json file for several networks parameters')

if __name__ == "__main__":
    args = parser.parse_args()

    if args.config:
        # in case of configuration file, we apply multi-processing generation of any combination of given parameters.
        # works only for fast graph generator (pandas-mode)
        with open(args.config) as json_file:
            args = json.load(json_file)
            num_cores = multiprocessing.cpu_count()
            parameters_combinations = itertools.product(args.nodes, args.steps, args.up, args.down, args.is_directed)
            results = Parallel(n_jobs=num_cores)(
                delayed(fdrg.fast_dynamic_er_random_graph)(*i) for i in parameters_combinations)
    else:
        if args.mode is 'pandas':
            fdrg.fast_dynamic_er_random_graph(n=args.nodes, steps=args.steps, up_rate=args.up, down_rate=args.down,
                                              write_to_csv=True, is_directed=args.directed,
                                              output_file_name=f'{args.out_file}.csv')
        else:  # NetworkX mode
            drg.dynamic_er_random_graph(n=args.nodes, steps=args.steps, up_rate=args.up, down_rate=args.down,
                                        is_directed=args.directed, write_to_file=True, output_file_name=args.out_file)
