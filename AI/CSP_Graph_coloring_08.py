# Function to check if it's safe to assign a color to a vertex
def is_safe(graph, colors, vertex, c):
    for neighbor in graph[vertex]:
        if colors[neighbor] == c:
            return False
    return True

# Backtracking function to solve the graph coloring problem
def graph_coloring(graph, m, colors, vertex):
    # If all vertices are assigned a color then return True
    if vertex == len(graph):
        return True

    # Consider this vertex and try different colors
    for c in range(1, m + 1):
        # Check if assignment of color c to vertex is safe
        if is_safe(graph, colors, vertex, c):
            colors[vertex] = c  # Assign color c to vertex

            # Recur to assign colors to the rest of the vertices
            if graph_coloring(graph, m, colors, vertex + 1):
                return True

            # If assigning color c doesn't lead to a solution, backtrack
            colors[vertex] = 0

    return False

# Function to solve the graph coloring problem
def solve_graph_coloring(graph, m):
    colors = [0] * len(graph)  # List to store colors assigned to vertices

    if not graph_coloring(graph, m, colors, 0):
        print("Solution does not exist")
        return False

    # Print the color assignments
    print_solution(colors)
    return True

# Function to print the solution
def print_solution(colors):
    for i in range(len(colors)):
        print(f"Vertex {i}: Color {colors[i]}")

# Example usage:
# Represent the graph as an adjacency list
graph = [
    [1, 2],        # Vertex 0 is connected to Vertex 1, 2
    [0, 2],        # Vertex 1 is connected to Vertex 0, 2
    [0, 1, 3],     # Vertex 2 is connected to Vertex 0, 1, 3
    [2, 4],        # Vertex 3 is connected to Vertex 2, 4
    [3]            # Vertex 4 is connected to Vertex 3
]

m = 3  # Number of colors
solve_graph_coloring(graph, m)
