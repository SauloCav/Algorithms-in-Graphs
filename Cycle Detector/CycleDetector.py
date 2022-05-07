#! /usr/bin/env python3
# -*- coding: utf-8 -*-

class Graph:
 
    def __init__(self, edges, numNodes):
 
        self.adjacencyList = [[] for _ in range(numNodes)] #É criada uma lista de adjacências com o número de nós passado

        #Cada um dos vertices passados são adicionados na lista
        for (source, destination) in edges:
            self.adjacencyList[source].append(destination)
            self.adjacencyList[destination].append(source)

def DFS_Traversal(graph, v, visited, parent_node =- 1):
 
    visited[v] = True #Marca o nó atual como true

    for u in graph.adjacencyList[v]: #Para cada vértice é feita a análise
        if not visited[u]: #Se u não é visitado é feita uma re-análise
            if DFS_Traversal(graph, u, visited, v):
                return True
        elif u != parent_node: #Se u for visitado e não é um nó parente então há um ciclo
            return True

    return False
 
 
if __name__ == '__main__':
 
    edges = [ (0, 1), (0, 2), (2, 3), (2, 4), (3, 4) ] #Definição dos vertices
 
    numNodes = 5 #Numero de nós do grafo

    constructed_graph = Graph(edges, numNodes) #Os vértices e o número de nós são então enviados para a montagem do grafo

    visited = [False] * numNodes #Passa os nós visitados e não visitados

    #DFS_Traversal é chamada
    if DFS_Traversal(constructed_graph, 0, visited):
        print('Um Ciclo Detectado!')
    else:
        print('Nenhum Ciclo foi Detectado!')
