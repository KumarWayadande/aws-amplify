def dfs(graph, vertex, visited=None):
    if visited is None:
        visited = set()

    # Mark the current node as visited
    visited.add(vertex)
    print(vertex)  # You can collect this in a list if needed

    # Recur for all the vertices adjacent to this vertex
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

    return visited

# Example of an undirected graph using adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Run DFS starting from vertex 'A'
dfs(graph, 'A')
