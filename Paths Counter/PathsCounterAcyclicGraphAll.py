#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from itertools import permutations

class Graph:

	def __init__(self, V):
		self.V = V
		self.adj = [[] for i in range(V)]

	def addEdge(self, u, v):
		self.adj[u].append(v)

	def isCyclicUtil(self, v, visited, recStack):
		visited[v] = True
		recStack[v] = True

		for neighbour in self.adj[v]:
			if visited[neighbour] == False:
				if self.isCyclicUtil(neighbour, visited, recStack) == True:
					return True
			elif recStack[neighbour] == True:
				return True
    
		recStack[v] = False
		return False

	def isCyclic(self):
		visited = [False] * (self.V + 1)
		recStack = [False] * (self.V + 1)
		for node in range(self.V):
			if visited[node] == False:
				if self.isCyclicUtil(node,visited,recStack) == True:
					return True
		return False
	
	def countPathsUtil(self, u, d, visited, pathCount):
		visited[u] = True

		if (u == d):
			pathCount[0] += 1
		else:
			i = 0
			while i < len(self.adj[u]):
				if (not visited[self.adj[u][i]]):
					self.countPathsUtil(self.adj[u][i], d, visited, pathCount)
				i += 1

		visited[u] = False

	def countPaths(self, s, d):
		visited = [False] * self.V

		pathCount = [0]
		self.countPathsUtil(s, d, visited, pathCount)
		return pathCount[0]


if __name__ == '__main__':

	numNodes = 4

	g = Graph(numNodes)
	g.addEdge(0, 1)
	g.addEdge(0, 2)
	g.addEdge(0, 3)
	g.addEdge(1, 3)

	if g.isCyclic() == 1:
		print ("Graph has a cycle")
	else:

		comb = permutations([0, 1, 2, 3], 2)
		numPaths = 0

		for i in list(comb):
			numPaths = numPaths + (g.countPaths(i[0], i[1]))
		
		print("Total de Caminhos: ", numPaths)
