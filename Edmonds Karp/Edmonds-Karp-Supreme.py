#! /usr/bin/env python3
# -*- coding: utf-8 -*-

def bfs(C, F, s, t):
    stack = [s]
    paths={s:[]}
    if s == t:
            return paths[s]
    while(stack):
            u = stack.pop()
            for v in range(len(C)):
                    if(C[u][v]-F[u][v]>0) and v not in paths:
                            paths[v] = paths[u]+[(u,v)]
                            if v == t:
                                    return paths[v]
                            stack.append(v)
    return None

def maxFlow(C, s, t):
    n = len(C) # C is the capacity matrix
    F = [[0] * n for i in range(n)]
    path = bfs(C, F, s, t)
    while path != None:
        flow = min(C[u][v] - F[u][v] for u,v in path)
        for u,v in path:
            F[u][v] += flow
            F[v][u] -= flow
        path = bfs(C,F,s,t)
    return sum(F[s][i] for i in range(n))

C = [[ 0, 3, 3, 0, 0, 0 ],  # s
 [ 3, 0, 2, 3, 0, 0 ],  # o
 [ 0, 2, 0, 0, 2, 0 ],  # p
 [ 0, 0, 0, 0, 4, 2 ],  # q
 [ 0, 0, 0, 2, 0, 2 ],  # r
 [ 0, 0, 0, 0, 2, 0 ]]  # t

source = 0  # A
sink = 5    # F
maxVal = maxFlow(C, source, sink)
print("max_flow_value is: ", maxVal)