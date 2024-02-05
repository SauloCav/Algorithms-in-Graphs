STRONGLY-CONNECTED-COMPONENTS.G/
1 call DFS.G/ to compute finishing times u:f for each vertex u
2 compute GT
3 call DFS.GT/, but in the main loop of DFS, consider the vertices
in order of decreasing u:f (as computed in line 1)
4 output the vertices of each tree in the depth-first forest formed in line 3 as a
separate strongly connected component
