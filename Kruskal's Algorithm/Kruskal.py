#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import defaultdict

class Graph:

	# Constrói o grafo
	def __init__(self, vertices):
		self.V = vertices
		self.graph = []

	# Adiciona arestas
	def addEdge(self, u, v, w):
		self.graph.append([u, v, w])

	# Função que busca o conjunto de um elemento i
	def find(self, parent, i):
		if parent[i] == i:
			return i
		return self.find(parent, parent[i])

	# Função que une dois conjuntos de x e y
	def union(self, parent, rank, x, y):
		xroot = self.find(parent, x)
		yroot = self.find(parent, y)

		# Anexa uma árvore de menor classificação na raiz da árvore de classificação alta
		if rank[xroot] < rank[yroot]:
			parent[xroot] = yroot
		elif rank[xroot] > rank[yroot]:
			parent[yroot] = xroot
		else: # Se os ranks forem iguais, então um é feito raiz eo rank é incrementado em um
			parent[yroot] = xroot
			rank[xroot] += 1

	# Função principal para retornar MST
	def KruskalMST(self):
		result = [] # retorna a floresta resultante
		i = 0
		e = 0

		# Todas as arestas são ordenadas em ordem não decrescente de seu peso
		self.graph = sorted(self.graph, key=lambda item: item[2])

		parent = []
		rank = []

		for node in range(self.V):
			parent.append(node)
			rank.append(0)

		while e < self.V - 1:

			# A menor aresta é escolhida e o índice é incrementado para a próxima iteração
			u, v, w = self.graph[i]
			i = i + 1
			x = self.find(parent, u)
			y = self.find(parent, v)

			# Se incluir esta aresta não causar ciclo, inclua-a no resultado e incremente o índice do resultado para a próxima aresta. Caso contrário ele é descartado
			if x != y:
				e = e + 1
				result.append([u, v, w])
				self.union(parent, rank, x, y)

		# Printando MST
		mstWeight = 0
		print ("MST edges:")
		for u, v, weight in result:
			mstWeight += weight
			print("%d, %d - %d" % (u, v, weight))

		print("MST Weight: " , mstWeight)

g = Graph(4)
g.addEdge(0, 1, 1)
g.addEdge(0, 2, 10)
g.addEdge(0, 3, 2)
g.addEdge(1, 3, 2)

#Grafo com ciclo negativo
#g = Graph(3)
#g.addEdge(0, 1, 1)
#g.addEdge(0, 2, 2)
#g.addEdge(1, 0, -2)

g.KruskalMST()
