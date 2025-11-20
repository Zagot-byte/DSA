def prim(G):
    INF = 9999999
    N = len(G)
    selected_vertex = [False] * N
    selected_vertex[0] = True
    no_of_edges = 0
    total = 0

    print("Edge : Weight")
    while no_of_edges < N - 1:
        min_dist = INF
        x = 0
        y = 0
        for i in range(N):
            if selected_vertex[i]:
                for j in range(N):
                    if not selected_vertex[j] and G[i][j]:
                        if min_dist > G[i][j]:
                            min_dist = G[i][j]
                            x, y = i, j
        print("Edge (", x, ",", y, ") and weight =", G[x][y])
        total += G[x][y]
        selected_vertex[y] = True
        no_of_edges += 1
    print("Total path Length =", total)
graph_adj = {
    'A': [('B',2), ('C',3)],
    'B': [('A',2), ('D',4), ('E',1)],
    'C': [('A',3), ('D',5)],
    'D': [('B',4), ('C',5), ('E',7)],
    'E': [('B',1), ('D',7)],
}

    A
   / \
  B   C
 / \  / 
E   D   

