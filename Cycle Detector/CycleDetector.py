#! /usr/bin/env python3
# -*- coding: utf-8 -*-

class Graph:
 
    def __init__(self, edges, a):
 
        self.adjacencyList = [[] for _ in range(a)]
 
        for (source, destination) in edges:
            self.adjacencyList[source].append(destination)
            self.adjacencyList[destination].append(source)

def DFS_Traversal(graph, v, visited, parent_node=-1):
 
    visited[v] = True

    for u in graph.adjacencyList[v]:
        if not visited[u]:
            if DFS_Traversal(graph, u, visited, v):
                return True
        elif u != parent_node:
            return True

    return False
 
 
if __name__ == '__main__':
 
    edges = [
        (0, 1), (0, 2), (2, 3), (2, 4), (3, 4)
    ]
 
    a = 5

    constructed_graph = Graph(edges, a)

    visited = [False] * a

    if DFS_Traversal(constructed_graph, 0, visited):
        print('Cycle detected')
    else:
        print('Cycle not detected')