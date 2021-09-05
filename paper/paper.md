---  
title: 'DynamicRandomGraphs: A Python package for generation of temporal random graphs'

tags:

- Python
- Network Science
- Temporal Networks
- Random Graphs

authors:

- name: Yanir Marmor affiliation: 1
- name: Alex Z. Abbey affiliation: 1
- name: Osnat Mokryn affiliation: 1  
  affiliations:
- name: University of Haifa index: 1

date: 27 June 2021 bibliography: paper.bib link-citations: yes

# Summary

Large-scale real-world interaction systems, such as social, technological, and biological networks, are dynamic
structures that change with time. There is an increased interest in studying the dynamics and temporal evolution of
these systems. One of the ways is by modeling these systems using dynamic temporal networks.

Models for studying networks are primarily static. Lately, the work in `[@Zhang:2017]` offered natural generalizations
to the dynamic case of several static network models, where one assumes that continuous-time Markov processes govern the
appearance and disappearance of edges. Thus, the fundamental unit of analysis is the entire history of the network.
Edges appear and disappear by making transitions from present to absent or vice versa at certain rates. For example, in
temporal random networks, the rate depends on the required probability of having an edge between any two nodes
(vertices). Such temporal modeling is also significant for the research and understanding of virality and epidemics:
airborne diseases spread over networks of contacts between individuals that change in time, and ideas dynamically spread
over social networks.

`RandomDynamicGraph` is a Python package that implements the algorithm from `[@Zhang:2017]`  for generating large-scale
dynamic random graphs. The package focuses on massive data generation; it uses efficient math calculations, writes to
file instead of in-memory when datasets are too large, and it supports multi-processing.

`DynamicRandomGraphs` was created for use by network scientists and other researchers who use temporal networks to
represent their data, as well as students in courses on dynamic networks, complex networks, and networks science. The
package was first used to simulate the spread of Covid-19 under different social distancing conditions as presented in
Networks 2021: [Reducing temporal density reduces total infection rate](https://www.youtube.com/watch?v=gUyP7etPPvE).

# Statement of need

Lack of real-life temporal network data due to data collection cost, user privacy, and up-to-date and relevant
information issues creates a need for temporal network models. Current temporal network models tend to be either static
or of small size.

This library permits in-depth theoretical and empirical analysis of large-scale temporal networks; it does so without
requiring a large investment in data collecting and without jeopardizing human privacy.

# Other packages

A popular software package is `NetworkX`. NetworkX is a great package for creating, manipulating, and studying complex
networks' structure, dynamics, and functions but is unsuitable for large temporal networks.
`DyNetx` is an extension of `NetworkX` for dynamic graphs. Unfortunately, Because of the dependence on NetworkX,
`DyNetx`'s performance is deficient in large-scale temporal networks.
`netrd` is another Python library based on the `NetworkX` interface and provides utilities for dynamic graphs. In the
context of random graph generation, there are some libraries in non-Python languages: `DANCer` (Scala), `randomGraph` (
Matlab), `Graph1`(C++), `grapherator`(R), `igraph`(R) etc.

In contrast to the other mentioned packages,`DynamicRandomGraphs`, suggested here, is a Python package associated with
dynamic networks that generate random temporal networks`[@Zhang:2017]`. Python allows the wrapping of low-level
languages for speed without sacrificing flexibility or user-friendliness in the user interface.
The `DynamicRandomGraphs` API was created to provide a class-based and user-friendly interface for generating
large-scale random dynamic networks efficiently. Conversion of `DynamicRandomGraphs` objects to `NetworkX` objects is
supported but inefficient.

# Support

Bug reports and feature requests are highly appreciated via the GitHub issue tracker.

# References