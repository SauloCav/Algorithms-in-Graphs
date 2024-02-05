# Elementary Graph Algorithms

## Representations of graphs

- We can choose between two standard ways to represent a graph G D .V; E/: as a collection of adjacency lists or as an adjacency matrix. Either way applies to both directed and undirected graphs.
- Because the adjacency-list representation provides a compact way to represent sparse graphs—those for which jEj is much less than jV j 2 —it is usually the method of choice.
- We may prefer an adjacency-matrix representation, however, when the graph is dense—jEj is close to jV j 2 —or when we need to be able to tell quickly if there is an edge connecting two given vertices.
- A potential disadvantage of the adjacency-list representation is that it provides no quicker way to determine whether a given edge .u; / is present in the graph than to search for  in the adjacency list AdjŒu.
- Like the adjacency-list representation of a graph, an adjacency matrix can represent a weighted graph. For example, if G D .V; E/ is a weighted graph with edgeweight function w, we can simply store the weight w.u; / of the edge .u; / 2 E as the entry in row u and column  of the adjacency matrix.
- Moreover, adjacency matrices carry a further advantage for unweighted graphs: they require only one bit per entry.
- Implementing vertex and edge attributes in real programs can be another story entirely. There is no one best way to store and access vertex and edge attributes.
- For a given situation, your decision will likely depend on the programming language you are using, the algorithm you are implementing, and how the rest of your program uses the graph.
- Many other ways of implementing attributes are possible. For example, in an object-oriented programming language, vertex attributes might be represented as instance variables within a subclass of a Vertex class.

## Breadth-first search

- Breadth-first search is one of the simplest algorithms for searching a graph and the archetype for many important graph algorithms.
- 



## Depth-first search




## Topological sort



## Strongly connected components








