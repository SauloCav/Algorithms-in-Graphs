DFS.G/
1 for each vertex u 2 G:V
2 u:color D WHITE
3 u: D NIL
4 time D 0
5 for each vertex u 2 G:V
6 if u:color = = WHITE
7 DFS-VISIT.G; u/

DFS-VISIT.G; u/
1 time D time C 1 // white vertex u has just been discovered
2 u:d D time
3 u:color D GRAY
4 for each  2 G:AdjŒu // explore edge .u; /
5 if :color == WHITE
6 : D u
7 DFS-VISIT.G; /
8 u:color D BLACK // blacken u; it is finished
9 time D time C 1
10 u:f D time
