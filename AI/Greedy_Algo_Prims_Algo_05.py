import heapq

def prim(graph, start):
    # Number of vertices in the graph
    n = len(graph)
    
    # Min-heap to store the edge (weight, vertex) pairs
    min_heap = []
    # Array to keep track of the vertices included in the MST
    in_mst = [False] * n
    # Start with the first vertex (start)
    in_mst[start] = True

    # Add all edges from the starting vertex to the heap
    for weight, vertex in graph[start]:
        heapq.heappush(min_heap, (weight, vertex))

    mst_edges = []  # To store the edges of the MST
    total_weight = 0  # To store the total weight of the MST

    # While there are still edges to process
    while min_heap:
        # Get the minimum edge from the heap
        weight, vertex = heapq.heappop(min_heap)

        # Skip if the vertex is already included in the MST
        if in_mst[vertex]:
            continue

        # Include this vertex in the MST
        in_mst[vertex] = True
        mst_edges.append((weight, vertex))
        total_weight += weight

        # Add all edges from this vertex to the heap
        for next_weight, next_vertex in graph[vertex]:
            if not in_mst[next_vertex]:
                heapq.heappush(min_heap, (next_weight, next_vertex))

    return mst_edges, total_weight

# Example usage:
# Represent the graph as an adjacency list
# graph[u] = [(weight, v), ...] where (u, v) is an edge with the given weight
graph = {
    0: [(2, 1), (3, 3)],
    1: [(2, 0), (4, 2)],
    2: [(4, 1), (5, 3)],
    3: [(3, 0), (5, 2)]
}

start_node = 0
mst_edges, total_weight = prim(graph, start_node)

print("Edges in MST:", mst_edges)
print("Total weight of MST:", total_weight)
