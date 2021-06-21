# RandDyNetx - Random dynamic networks generator

RandDyNetx provides implementations of dynamic networks in Python. It deals with the efficient generation of random dynamic (also known as *temporal*) networks.

The project documentation can be found on *ReadTheDocs*.

## Related works
* [NetworkX](https://networkx.org/) - a Python package for the creation, manipulation, and study of the structure, dynamics, and functions of complex networks (Great package, but not suitable for large networks or temporal networks).
* [DyNetx](https://dynetx.readthedocs.io/en/latest/index.html) - a Python software package that extends NetworkX with dynamic network models and algorithms (Excellent package, but performance in large-scale temporal networks is limited).
* [DANCer](https://perso.univ-st-etienne.fr/largeron/DANCer_Generator/#reference) - a Scala software that generates dynamic attributed networks with community structure that follow the known properties of
real-world networks ([paper](https://hal-auf.archives-ouvertes.fr/hal-01377321/document)).
* [pathpy](https://www.pathpy.net/) - an Open Source python package providing higher-order network analytics for time series data.
* [TACOMA](https://github.com/benmaier/tacoma) - TemporAl COntact Modeling and Analysis. Provides fast tools to analyze temporal contact networks, produce surrogate networks using qualitative models and simulate Gillespie processes on them. TACOMA is a joint C++/Python-package for the modeling and analysis of undirected and unweighted temporal networks, with a focus on (but not limited to) human face-to-face contact networks.
* [Teneto](https://teneto.readthedocs.io/en/latest/index.html) - a Python package includes various tools for analyzing temporal network data. Temporal network measures, temporal network generation, derivation of time-varying/dynamic connectivities, plotting functions.
* [netrd](https://netrd.readthedocs.io/en/latest/) - This library provides a consistent, NetworkX-based interface to various utilities for graph distances, graph reconstruction from time series data, and simulated dynamics on networks.
* [Random Modular Network Generator](https://github.com/prathasah/random-modular-network-generator) Generates random graphs with tunable strength of community structure
* [randomGraph](https://github.com/sdghafouri/randomGraph) very simple random graph generator in matlab
* [Graph1](https://github.com/Saptaparni/Graph1) Random Graph Generator with Max capacity paths (C++)
* [grapherator](https://github.com/jakobbossek/grapherator) - The R package grapherator implements a modular approach to benachmark graph generation focusing on undirected, weighted graphs.
* [igraph: Network Analysis and Visualization](https://cran.r-project.org/package=igraph) This R package Includes some methods to generate classical Erdos-Renyi random graphs as well as more recent models, e.g., small-world graphs.
* [netgen: Network Generator for Combinatorial Graph Problems](https://cran.r-project.org/package=netgen) This R package Contains some methods to generate complete graphs especially for benchmarking Travelling-Salesperson-Problem solvers.
* [bnlearn: Bayesian Network Structure Learning, Parameter Learning and Inference](https://cran.r-project.org/web/packages/bnlearn/index.html) The R function `bnlearn::random.graph` implements some algorithms to create graphs.


## Papers
* Zhang, X., Moore, C. & Newman, M.E.J. [Random graph models for dynamic networks](https://link.springer.com/article/10.1140%2Fepjb%2Fe2017-80122-8#citeas). Eur. Phys. J. B 90, 200 (2017). [doi](https://doi.org/10.1140/epjb/e2017-80122-8)
* Peixoto, T.P., Rosvall, M. [Modelling sequences and temporal networks with dynamic community structures](https://www.nature.com/articles/s41467-017-00148-9). Nat Commun 8, 582 (2017). [doi](https://doi.org/10.1038/s41467-017-00148-9)
