#! /usr/bin/env python3
# -*- coding: utf-8 -*-

class Graph(object):
   def __init__(self, num_vertices):
       self.V = num_vertices
       self.graph = []
  
   def add_edge(self, u, v, w):
       self.graph.append([u, v, w])
  
   def find(self, root, i):
       if root[i] == i:
           return i
       print(i, root[i])
       return self.find(root, root[i])
  
   def union(self, root, rank, x, y):
       print(f"root: {root}, rank: {rank}")
       xroot = self.find(root, x)
       yroot = self.find(root, y)
       if rank[xroot] < rank[yroot]:
           root[xroot] = yroot
       elif rank[xroot] > rank[yroot]:
           root[yroot] = xroot
       else:
           root[yroot] = xroot
           rank[xroot] += 1
       print(f"root: {root}, rank: {rank}")
  

   def kruskals(self):

       result = []

       i, e  = 0, 0

       self.graph = sorted(self.graph, key = lambda item: item[2])

       root = []
       rank = []
       for node in range(self.V):
           root.append(node)
           rank.append(0)
 
       while e < self.V - 1:
           u, v, w = self.graph[i]
           i = i + 1
           x = self.find(root, u)
           y = self.find(root, v)
           print(f"x, y: {x}, {y}")
           if x != y:
               e = e + 1
               result.append([u, v, w])
               self.union(root, rank, x, y)
 
       for u, v, w in result:
           print(f'{u} - {v}: {w}')
      
g = Graph(6)
g.add_edge(0, 1, 4)
g.add_edge(0, 2, 4)
g.add_edge(1, 2, 2)
g.add_edge(1, 0, 4)
g.add_edge(2, 0, 4)
g.add_edge(2, 1, 2)
g.add_edge(2, 3, 3)
g.add_edge(2, 5, 2)
g.add_edge(2, 4, 4)
g.add_edge(3, 2, 3)
g.add_edge(3, 4, 3)
g.add_edge(4, 2, 4)
g.add_edge(4, 3, 3)
g.add_edge(5, 2, 2)
g.add_edge(5, 4, 3)
g.kruskals()
