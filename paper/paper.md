---  
title: 'DynamicRandomGraphs: A Python package for generation of dynamic graphs randomly'

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

A temporal network, also known as a dynamic network, is a network representation that changes over time. It is extremely
valuable for examining how a connected system, such as a social or biological system, grows, changes, or evolves through
time. This temporal representation can demonstrate how a viral infection spreads with a human population or how  
information circulates in a social network.

Network research has advanced at a rapid pace in recent years, as have the insights that have emerged from it, as has  
research that employs tools from network science in the study of social networks, biological networks, neurological  
networks, communication networks, energy, and other topics.

`DynamicRandomGraphs` is a Python package that implements a basic method for generating large-scale random  
dynamic graphs. The package's focus is on massive and efficient data generation; it uses efficient math calculations,
writes the data to disk instead of in-memory when datasets are too large, and supports multi-processing.

`DynamicRandomGraphs`
was created for use by network scientists and other researchers who use temporal networks to represent their data, as
well as students in courses on dynamic networks, complex networks, and networks science. The package was first used to
simulate the spread of Covid-19 under different social distancing conditions as presented in Networks 2021:
[Reducing temporal density reduces total infection rate](https://www.youtube.com/watch?v=gUyP7etPPvE).

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
dynamic networks that generate random temporal networks`[@Zhang:2017]`. Python allows the wrapping of low-level languages for speed
without sacrificing flexibility or user-friendliness in the user interface. The `DynamicRandomGraphs` API was created to
provide a class-based and user-friendly interface for generating large-scale random dynamic networks efficiently.
Conversion of `DynamicRandomGraphs` objects to `NetworkX` objects is supported but inefficient.

# Support

Bug reports and feature requests are highly appreciated via the GitHub issue tracker.

# References