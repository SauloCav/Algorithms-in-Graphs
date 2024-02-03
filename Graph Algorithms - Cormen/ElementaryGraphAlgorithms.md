# Elementary Graph Algorithms

## Representations of graphs

- We can choose between two standard ways to represent a graph G D .V; E/: as a collection of adjacency lists or as an adjacency matrix. Either way applies to both directed and undirected graphs. Because the adjacency-list representation provides a compact way to represent sparse graphs—those for which jEj is much less than jV j 2 —it is usually the method of choice. Most of the graph algorithms presented in this book assume that an input graph is represented in adjacencylist form. We may prefer an adjacency-matrix representation, however, when the graph is dense—jEj is close to jV j 2 —or when we need to be able to tell quickly if there is an edge connecting two given vertices.
