#! /usr/bin/env python3
# -*- coding: utf-8 -*-
 
class Graph:
 
    def __init__(self, V):
        self.V = V
        self.adj = [[] for i in range(V)]
 
    def addEdge(self, u, v):
 
        self.adj[u].append(v)

    def countPaths(self, s, d):

        visited = [False] * self.V

        pathCount = [0]
        self.countPathsUtil(s, d, visited, pathCount)
        return pathCount[0]

    def countPathsUtil(self, u, d,
                       visited, pathCount):
        visited[u] = True
 
        if (u == d):
            pathCount[0] += 1

        else:

            i = 0
            while i < len(self.adj[u]):
                if (not visited[self.adj[u][i]]):
                    self.countPathsUtil(self.adj[u][i], d,
                                        visited, pathCount)
                i += 1
 
        visited[u] = False
 
if __name__ == '__main__':

    vertices = 4

    g = Graph(vertices)
    g.addEdge(0, 1)	
    g.addEdge(0, 2)
    g.addEdge(0, 3)
    g.addEdge(2, 0)
    g.addEdge(2, 1)
    g.addEdge(1, 3)
 
    s = 0
    d = 1
    pathCount = 0
    
    for i in range(vertices - 1):
        path = g.countPaths(s, d)
        print(s, "-", d, "|" , path)
        s = s + 1
        d = d + 1
        pathCount = pathCount + path
    
    print("Soma de todos os Caminhos: ", pathCount)
