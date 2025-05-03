from collections import deque

def bfs_recursive(graph, queue, visited):
    if not queue:
        return

    vertex = queue.popleft()
    print(vertex)  # You can collect this in a list if needed

    for neighbor in graph[vertex]:
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)

    bfs_recursive(graph, queue, visited)

# Example of an undirected graph using adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Initialization
start_node = 'A'
visited = set([start_node])
queue = deque([start_node])

# Run BFS
bfs_recursive(graph, queue, visited)
