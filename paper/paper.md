---
title: 'RandomDynamicGraph: A Python package for generation of dynamic graphs randomly' tags:

- Python
- Network Science
- Temporal Networks
- Random Graphs

authors:

- name: Yanir Marmor affiliation: "1"
- name: Alex Z. Abbey affiliation: "1"
- name: Ossi Mokryn affiliation: "2"
  affiliations:
- name: Tel Aviv University index: 1
- name:University of Haifa index: 2

date: 27 June 2021 bibliography: paper.bib link-citations: yes

# Summary

A temporal network, also known as a dynamic network, is a network representation that changes over time. It is extremely
valuable for examining how a connected system, such as a social or biological system, grows, changes, or evolves through
time. This temporal representation can demonstrate how a viral infection spreads with a human population or how
information circulates in a social network.

Network research has advanced at a rapid pace in recent years, as have the insights that have emerged from it, as has
research that employs tools from network science in the study of social networks, biological networks, neurological
networks, communication networks, energy, and other topics.

`RandomDynamicGraph` is a Python package that implements three different methods for generating large-scale random
dynamic graphs. The package's focus is on massive data generation; it uses efficient math calculations, writes to file
instead of in-memory when datasets are too large, and supports multi-processing.

# Statement of need

In the context of networks science, it appears that gathering relevant data is one of the most difficult challenges
facing researchers in the field. Despite the fact that we live in the digital era, issues of data collection cost, user
privacy, up-to-date and relevant information are a barrier for researchers who are forced to use partial, old, and not
always relevant data.

Furthermore, despite the fact that one of the distinguishing characteristics of complex systems is their size,
researchers in the field are obliged to rely on small-scale data. And, despite the fact that networks are probabilistic,
research in the field use only individual networks, making it difficult to discern the probabilistic aspect.

In the mentioned circumstance, the utility of this library appears to be twofold: on the one hand, it permits in-depth
theoretical and empirical analysis of temporal networks; on the other hand, it does so without requiring a large
investment in data collecting and without jeopardizing human privacy.

Other software in the field that aids researchers depends on the popularity of graph and network analysis are `NetworkX`
that is a great package for the creation, manipulation, and study of the structure, dynamics, and functions of complex
networks, but not suitable for large networks or temporal networks. `DyNetx` is an extension of `NetworkX` for dynamic
graphs. Unfortunately, Because of the dependence on NetworkX, the DyNetx's performance is very low in large-scale
temporal networks. `netrd` is another Python library that based on NetworkX interface and provide utilities for dynamic
graphs. In the context of random graph generation there are some libraries in non-Python languages: DANCer (Scala),
randomGraph (Matlab), Graph1(C++), grapherator(R), igraph(R) etc.

`RandomDynamicGraph` is a Python package associated with dynamic networks that generates random temporal networks. Python
allows for the wrapping of low-level languages for speed without sacrificing flexibility or user-friendliness in the
user interface. The `RandomDynamicGraph` API was created to provide a class-based and user-friendly interface for efficient
generation of large-scale random dynamic networks.

Conversion of `RandomDynamicGraph` objects to `NetworkX` objects is supported, but NetworkX has no use during data generation
due to NetworkX's waste time running and volume of data.

`RandomDynamicGraph` was created for use by network scientists and other researchers who use temporal networks to represent
their data, as well as students in courses on dynamic networks, complex networks, and networks science.

It's already been used in few scientific research projects (*citation talk in NetSci*).

# Support

Bug reports and feature requests are highly appreciated via the GitHub issue tracker

# Citations

Citations to entries in paper.bib should be in
[rMarkdown](http://rmarkdown.rstudio.com/authoring_bibliographies_and_citations.html)
format.

If you want to cite a software repository URL (e.g. something on GitHub without a preferred citation) then you can do it
with the example BibTeX entry below for @fidgit.

For a quick reference, the following citation commands can be used:

- `@author:2001`  ->  "Author et al. (2001)"
- `[@author:2001]` -> "(Author et al., 2001)"
- `[@author1:2001; @author2:2001]` -> "(Author1 et al., 2001; Author2 et al., 2002)"

# Figures

Figures can be included like this:
![Caption for example figure.\label{fig:example}](figure.png)
and referenced from text using \autoref{fig:example}.

Figure sizes can be customized by adding an optional second parameter:
![Caption for example figure.](figure.png){ width=20% }

# Acknowledgements

We acknowledge contributions from Brigitta Sipocz, Syrtis Major, and Semyeong Oh, and support from Kathryn Johnston
during the genesis of this project.

# References