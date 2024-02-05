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
- Given a graph G D .V; E/ and a distinguished source vertex s, breadth-first search systematically explores the edges of G to “discover” every vertex that is reachable from s.
- It computes the distance (smallest number of edges) from s to each reachable vertex.
- It also produces a “breadth-first tree” with root s that contains all reachable vertices.
- For any vertex  reachable from s, the simple path in the breadth-first tree from s to  corresponds to a “shortest path” from s to  in G, that is, a path containing the smallest number of edges.
- The algorithm works on both directed and undirected graphs
- In graph theory, the shortest path problem is the problem of finding a path between two vertices (or nodes) in a graph such that the sum of the weights of its constituent edges is minimized.
- The most important algorithms for solving this problem are:
  - Dijkstra's algorithm solves the single-source shortest path problem with non-negative edge weight.
  - Bellman–Ford algorithm solves the single-source problem if edge weights may be negative.
  - A* search algorithm solves for single-pair shortest path using heuristics to try to speed up the search.
  - Floyd–Warshall algorithm solves all pairs shortest paths.
  - Johnson's algorithm solves all pairs shortest paths, and may be faster than Floyd–Warshall on sparse graphs.
  - Viterbi algorithm solves the shortest stochastic path problem with an additional probabilistic weight on each node.

## Depth-first search
- The strategy followed by depth-first search is, as its name implies, to search “deeper” in the graph whenever possible.
- Depth-first search explores edges out of the most recently discovered vertex  that still has unexplored edges leaving it. Once all of ’s edges have been explored, the search “backtracks” to explore edges leaving the vertex from which  was discovered.
- This process continues until we have discovered all the vertices that are reachable from the original source vertex. If any undiscovered vertices remain, then depth-first search selects one of them as a new source, and it repeats the search from that source.
- The algorithm repeats this entire process until it has discovered every vertex.

## Topological sort
- we can use depth-first search to perform a topological sort of a directed acyclic graph, or a “dag” as it is sometimes called.
- A topological sort of a dag G D .V; E/ is a linear ordering of all its vertices such that if G contains an edge .u; /, then u appears before  in the ordering. (If the graph contains a cycle, then no linear ordering is possible.)
- We can perform a topological sort in time ‚.V C E/, since depth-first search takes ‚.V C E/ time and it takes O.1/ time to insert each of the jV j vertices onto the front of the linked list.

## Strongly connected components
- Our algorithm for finding strongly connected components of a graph G D .V; E/ uses the transpose of G, which we defined in Exercise 22.1-3 to be the graph GT D .V; ET/, where ET D f.u; / W .; u/ 2 Eg. That is, ET consists of the edges of G with their directions reversed.
- Given an adjacency-list representation of G, the time to create GT is O.V C E/. It is interesting to observe that G and GT have exactly the same strongly connected components: u and  are reachable from each other in G if and only if they are reachable from each other in GT. Figure 22.9(b) shows the transpose of the graph in Figure 22.9(a), with the strongly connected components shaded.







