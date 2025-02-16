""" 
Print Adjacency List - Python Implementation
Concept: Adjacency List Representation of a Graph
An adjacency list is a way to represent a graph where:

Each node (vertex) has a list of nodes it is connected to.
Since the graph is undirected, each edge (u, v) should be stored in the list of both u and v.
0-based indexing means nodes are numbered from 0 to V-1.
Key Points:
Efficient Representation: Uses a list of lists (dictionary or defaultdict in Python) instead of a matrix.
Space Complexity: O(V + E) (Stores only existing edges).
Time Complexity: O(V + E) (Iterates through edges once)
"""
# Print Adjacency List - Undirected Graph Representation
# ------------------------------------------------------
# We are given V vertices and E edges.
# We need to construct and return the adjacency list representation.
# ------------------------------------------------------

from collections import defaultdict

def printAdjacencyList(V, edges):
    """
    Function to create an adjacency list for an undirected graph.

    :param V: Number of vertices (nodes)
    :param edges: List of edges (pairs of connected nodes)
    :return: Adjacency list representation of the graph
    """
    # Step 1: Initialize an adjacency list with empty lists for each vertex
    adj_list = defaultdict(list)
    
    # Step 2: Add edges to adjacency list
    for u, v in edges:
        adj_list[u].append(v)  # Add v to u's adjacency list
        adj_list[v].append(u)  # Add u to v's adjacency list (undirected)

    # Step 3: Convert to a standard list format and return
    return [sorted(adj_list[i]) for i in range(V)]  # Sorting for consistent output

# Example Test Cases
print(printAdjacencyList(5, [[0,1], [0,4], [4,1], [4,3], [1,3], [1,2], [3,2]]))
# Expected Output: [[1,4], [0,2,3,4], [1,3], [1,2,4], [0,1,3]]

print(printAdjacencyList(4, [[0,3], [0,2], [2,1]]))
# Expected Output: [[2,3], [2], [0,1], [0]]

"""" 
Time Complexity Analysis
Building adjacency list: O(E) (each edge is processed once).
Sorting (for consistent output): O(V log V) (only if needed).
Overall Complexity: O(V + E) (ignoring sorting).
Space Complexity
O(V + E) (only stores edges, efficient for sparse graphs).
Final Thoughts
✅ Efficient adjacency list representation.
✅ Beginner-friendly explanation & comments.
✅ Optimized with defaultdict for fast adjacency list creation.


"""