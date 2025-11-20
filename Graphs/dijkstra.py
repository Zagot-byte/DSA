def sp(graph, start):
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    visited = set()
    
    while visited != set(graph.keys()):
        current_node = min((node for node in graph if node not in visited), key=lambda node: distances[node])
        visited.add(current_node)
        
        for neighbor, weight in graph[current_node]:
            if neighbor not in visited:
                new_distance = distances[current_node] + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
    return distances
graph = {
    'A': [('B', 4), ('C', 7)],
    'B': [('A', 4), ('C', 8), ('D', 5), ('E', 2)],
    'C': [('A', 7), ('B', 8), ('F', 6)],
    'D': [('B', 5)],
    'E': [('B', 2)],
    'F': [('C', 6)]
}

      A
    /   \
  4/     \7
   B------C
  / \      \
2/   \5     \6
 E    D      F

