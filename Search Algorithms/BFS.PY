grafo = {
 'A' : ['B','C'],
 'B' : ['D', 'E'],
 'C' : ['F'],
 'D' : ['D'],
 'E' : ['F'],
 'F' : []
}

visitados = []
fila = []

def bfs(visitados, grafo, no):
    visitados.append(no)
    fila.append(no)
    while fila:
        s = fila.pop(0)
        print (s, end = " ")
        for vizinho in grafo[s]:
            if vizinho not in visitados:
                visitados.append(vizinho)
                fila.append(vizinho)

bfs(visitados, grafo, 'A')
