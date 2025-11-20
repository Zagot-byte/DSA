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
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['D'],
    'D': ['E'],
    'E': []
}