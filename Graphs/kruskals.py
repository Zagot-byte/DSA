def kruskal(graph):
    result = []
    i, e = 0, 0
    graph = sorted(graph, key=lambda item: item[2])
    parent = []
    rank = []
    
    # Create disjoint sets
    def find(parent, i):
        if parent[i] == i:
            return i
        return find(parent, parent[i])
    
    def union(parent, rank, x, y):
        xroot = find(parent, x)
        yroot = find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    V = len(set([u for u, v, w in graph] + [v for u, v, w in graph]))  # Number of vertices
    parent = [i for i in range(V)]
    rank = [0] * V

    while e < V - 1:
        u, v, w = graph[i]
        i += 1
        x = find(parent, u)
        y = find(parent, v)
        if x != y:
            e += 1
            result.append((u, v, w))
            union(parent, rank, x, y)
    return result
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['D'],
    'D': ['E'],
    'E': []
}