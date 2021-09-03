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

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>

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
date. If you want to be safe, take a look at the [guide to installing Python packages](https://packaging.python.org/tutorials/installing-packages/). 

Clone the codebase from this github repository with the small green icon on the up-right corner `Code` or from the terminal: 
```shell
git clone ScanLab-ossi/random_dynamic_graph
```

Then, install the required packages:
```sh
 pip install -r requirements.txt
 ```



# License

# Roadmap

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
  connectivities, plotting functions.
* [netrd](https://netrd.readthedocs.io/en/latest/) - This library provides a consistent, NetworkX-based interface to
  various utilities for graph distances, graph reconstruction from time series data, and simulated dynamics on networks.
* [Random Modular Network Generator](https://github.com/prathasah/random-modular-network-generator) Generates random
  graphs with tunable strength of community structure
* [randomGraph](https://github.com/sdghafouri/randomGraph) very simple random graph generator in matlab
* [Graph1](https://github.com/Saptaparni/Graph1) Random Graph Generator with Max capacity paths (C++)
* [grapherator](https://github.com/jakobbossek/grapherator) - The R package grapherator implements a modular approach to
  benachmark graph generation focusing on undirected, weighted graphs.
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

