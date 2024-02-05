BFS.G; s/
1 for each vertex u 2 G:V  fsg
2 u:color D WHITE
3 u:d D 1
4 u: D NIL
5 s:color D GRAY
6 s:d D 0
7 s: D NIL
8 Q D ;
9 ENQUEUE.Q; s/
10 while Q ¤ ;
11 u D DEQUEUE.Q/
12 for each  2 G:AdjŒu
13 if :color = = WHITE
14 :color D GRAY
15 :d D u:d C 1
16 : D u
17 ENQUEUE.Q; /
18 u:color D BLACK
