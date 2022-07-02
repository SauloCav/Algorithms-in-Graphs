
def max_flow(C, s, t):
        n = len(C)
        F = [[0] * n for i in xrange(n)]
        path = bfs(C, F, s, t)
        while path != None:
            flow = min(C[u][v] - F[u][v] for u,v in path)
            for u,v in path:
                F[u][v] += flow
                F[v][u] -= flow
            path = bfs(C, F, s, t)
        return sum(F[s][i] for i in xrange(n))

def bfs(C, F, s, t):
        queue = [s]
        paths = {s:[]}
        if s == t:
            return paths[s]
        while queue: 
            u = queue.pop(0)
            for v in xrange(len(C)):
                    if(C[u][v]-F[u][v]>0) and v not in paths:
                        paths[v] = paths[u]+[(u,v)]
                        print paths
                        if v == t:
                            return paths[v]
                        queue.append(v)
        return None
    
C = [[ 0, 3, 3, 0, 0, 0 ],
     [ 0, 0, 2, 3, 0, 0 ],
     [ 0, 0, 0, 0, 2, 0 ],
     [ 0, 0, 0, 0, 4, 2 ],
     [ 0, 0, 0, 0, 0, 2 ],
     [ 0, 0, 0, 0, 0, 3 ]]

source = 0 
sink = 5 
max_flow_value = max_flow(C, source, sink)
print "Edmonds-Karp algorithm"
print "max_flow_value is: ", max_flow_value
