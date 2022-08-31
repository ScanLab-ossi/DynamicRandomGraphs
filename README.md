
# DynamicRandomGraphs: A Python package for generation of scalable temporal random graphs
[![No Maintenance Intended](http://unmaintained.tech/badge.svg)](http://unmaintained.tech/)

<!-- ABOUT THE PROJECT -->

## About The Project

DynamicRandomGraphs provides implementations of dynamic networks in Python. It deals with the efficient generation of
scalable dynamic (temporal) random networks.

The package was first used to simulate the spread of Covid-19 under different social distancing conditions as presented
in Networks 2021 and in Arxiv paper titled: An interaction-based contagion model over temporal networks demonstrates that reducing temporal network density reduces total infection rate. 
When using the package please cite the Arxiv paper: 
Abbey, A., Marmor, Y., Shahar, Y., Mokryn, O. (2022). An interaction-based contagion model over temporal networks demonstrates that reducing temporal network density reduces total infection rate. ArXiv 2202.11591, 1–21. https://arxiv.org/abs/2202.11591

The talk at Networks2021: [Reducing temporal density reduces total infection rate](https://www.youtube.com/watch?v=gUyP7etPPvE)

<!-- GETTING STARTED -->

# Getting started

## Prerequisites

Make sure you have `Python3` installed on your computer, as well as `pip` and `setuptools`, and that they are up to
date. If you want to be safe, take a look at
the [guide to installing Python packages](https://packaging.python.org/tutorials/installing-packages/).

Clone the codebase from this GitHub repository with the small green icon on the up-right corner `Code` or from the
terminal:

```shell
git clone ScanLab-ossi/random_dynamic_graph
```

Then, install the required packages:

```sh
 pip install -r requirements.txt
 ```

## Usage

Our package operates in two modes. A stand-alone mode allows for the generation of a series of graphs representing the
temporal network of choice; The parallel mode creates a set of temporal networks, each consisting of multiple graphs,
according to a predefined set of parameters.

### Stand-alone mode

```shell
python -m random_graph_generator --node=100 --steps=200 --mode="pandas"
```

This command will create network with 100 nodes along 200 time steps. That information will be saved as CSV file.

Similar example will create NetworkX object, and the relevant command is:

```shell
python -m random_graph_generator --node=100 --steps=200 --mode="NetworkX"
```

Other parameters are accessible for that mode:

```
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
```

### Parallel mode

Many networks can be created in parallel in this mode of operation. To do so, use the JSON file as the `
conf_example.json``.

```shell
python -m random_graph_generator --config="conf_example.json"
```

The json example looks like:

```json
{
  "nodes": [
    100,
    200,
    500
  ],
  "steps": [
    1000,
    2000
  ],
  "up": [
    0.001,
    0.005
  ],
  "down": [
    0.2,
    0.4
  ],
  "is_directed": [
    false
  ]
}
```

The generator makes a graph from every combination of parameters in the lists. From the example above, the generator
creates 24 different networks.

# License

Distributed under the MIT License. See `LICENSE` for more information.

Cite: 
Abbey, A., Marmor, Y., Shahar, Y.,Mokryn, O. (2022). An interaction-based contagion model over temporal networks demonstrates that reducing temporal network density reduces total infection rate. ArXiv 2202.11591, 1–21. https://arxiv.org/abs/2202.11591

# Roadmap

See the [open issues](https://github.com/ScanLab-ossi/random_dynamic_graph/issues) for a list of proposed features (and
known issues).

In general, we would like to extend the model for better control on the parameters on the time-line and on the degrees
distribution and communities parameters as well.

## Contributing

Feel free to fork and help out.

Test using `pytest`. Run slower tests with `pytest --runslow`.

## Related works

* [NetworkX](https://networkx.org/) - a Python package for the creation, manipulation, and study of the structure,
  dynamics, and functions of complex networks (Great package, but not suitable for large networks or temporal networks).
* [DyNetx](https://dynetx.readthedocs.io/en/latest/index.html) - a Python software package that extends NetworkX with
  dynamic network models and algorithms (Excellent package, but performance in large-scale temporal networks is limited)
  .
* [DANCer](https://perso.univ-st-etienne.fr/largeron/DANCer_Generator/#reference) - a Scala software that generates
  dynamic attributed networks with community structure that follow the known properties of real-world
  networks ([paper](https://hal-auf.archives-ouvertes.fr/hal-01377321/document)).
* [pathpy](https://www.pathpy.net/) - an Open Source python package providing higher-order network analytics for time
  series data.
* [TACOMA](https://github.com/benmaier/tacoma) - TemporAl COntact Modeling and Analysis. Provides fast tools to analyze
  temporal contact networks, produce surrogate networks using qualitative models and simulate Gillespie processes on
  them. TACOMA is a joint C++/Python-package for the modeling and analysis of undirected and unweighted temporal
  networks, with a focus on (but not limited to) human face-to-face contact networks.
* [Teneto](https://teneto.readthedocs.io/en/latest/index.html) - a Python package includes various tools for analyzing
  temporal network data. Temporal network measures, temporal network generation, derivation of time-varying/dynamic
  connectivity, plotting functions.
* [netrd](https://netrd.readthedocs.io/en/latest/) - This library provides a consistent, NetworkX-based interface to
  various utilities for graph distances, graph reconstruction from time series data, and simulated dynamics on networks.
* [Random Modular Network Generator](https://github.com/prathasah/random-modular-network-generator) Generates random
  graphs with tunable strength of community structure
* [randomGraph](https://github.com/sdghafouri/randomGraph) very simple random graph generator in matlab
* [Graph1](https://github.com/Saptaparni/Graph1) Random Graph Generator with Max capacity paths (C++)
* [grapherator](https://github.com/jakobbossek/grapherator) - The R package grapherator implements a modular approach to
  benchmark graph generation focusing on undirected, weighted graphs.
* [igraph: Network Analysis and Visualization](https://cran.r-project.org/package=igraph) This R package Includes some
  methods to generate classical Erdos-Renyi random graphs as well as more recent models, e.g., small-world graphs.
* [netgen: Network Generator for Combinatorial Graph Problems](https://cran.r-project.org/package=netgen) This R package
  Contains some methods to generate complete graphs especially for benchmarking Travelling-Salesperson-Problem solvers.
* [bnlearn: Bayesian Network Structure Learning, Parameter Learning and Inference](https://cran.r-project.org/web/packages/bnlearn/index.html)
  The R function `bnlearn::random.graph` implements some algorithms to create graphs.

## How to report issues?

Running into any bugs? Check out the [open issues](https://github.com/ScanLab-ossi/random_dynamic_graph/issues) to see
if we're already working on it. If not, open up a new issue, and we will check it out when we can. Thank you.



