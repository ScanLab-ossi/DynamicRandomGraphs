<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]


# RandomDynamicGraph - Random dynamic networks generator

<!-- ABOUT THE PROJECT -->

## About The Project

RandomDynamicGraph provides implementations of dynamic networks in Python. It deals with the efficient generation of
random dynamic (also known as *temporal*) networks.

### Built With

..

<!-- GETTING STARTED -->

# Getting started

If you want to use the library to generate random networks, you should follow these steps.

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

The graph generator can operate in two different modes. Working modes include creating a single network and quickly
generating a variety of networks.

### Single network mode

```shell
python random_graph_generator.py --node=100 --steps=200 --mode="pandas"
```

This command will crate network with 100 nodes along 200 time steps. That information will be saved as CSV file.

Similar example will create NetworkX object, and the relevant command is:

```shell
python random_graph_generator.py --node=100 --steps=200 --mode="NetworkX"
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

### Multi network mode

Many networks can be created in parallel in this mode of operation. To do so, use the JSON file as the `
conf_example.json``.

```shell
python random_graph_generator.py --config="conf_example.json"
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

# Roadmap

See the [open issues](https://github.com/othneildrew/Best-README-Template/issues) for a list of proposed features (and
known issues).

In general, we would like to extend the model for better control on the parameters on the time-line and on the
degrees distribution and communities parameters as well.

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

## Papers

* Zhang, X., Moore, C. & Newman,
  M.E.J. [Random graph models for dynamic networks](https://link.springer.com/article/10.1140%2Fepjb%2Fe2017-80122-8#citeas)
  . Eur. Phys. J. B 90, 200 (2017). [doi](https://doi.org/10.1140/epjb/e2017-80122-8)

## How to report issues?

Running into any bugs? Check out the [open issues](https://github.com/ScanLab-ossi/random_dynamic_graph/issues) to see
if we're already working on it. If not, open up a new issue, and we will check it out when we can. Thank you.



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png