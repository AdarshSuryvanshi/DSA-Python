""" 
Breadth-First Search (BFS) - Python Implementation
Concept: Breadth-First Search (BFS) Traversal of a Graph
Breadth-First Search (BFS) is a traversal algorithm for graphs:

Uses a queue (FIFO) to explore neighbors level by level.
Starts from vertex 0 and explores its adjacent vertices before moving to their neighbors.
Ensures that each node is visited only once using a visited list.
Key Points:
Uses a queue for BFS traversal (First In, First Out).
Time Complexity: O(V + E) (Visits each vertex and its edges once).
Space Complexity: O(V) (Stores visited nodes & queue).
Ensures traversal order follows adjacency list sequence.

"""
# --------------------------------------------------------
# Breadth-First Search (BFS) of a Graph
# --------------------------------------------------------
# Given an adjacency list `adj`, perform BFS traversal starting from node 0.
# --------------------------------------------------------

from collections import deque

def bfsOfGraph(adj):
    """
    Function to perform BFS traversal on a given adjacency list representation of a graph.

    :param adj: List of lists representing the adjacency list
    :return: List containing BFS traversal order
    """
    V = len(adj)  # Number of vertices
    visited = [False] * V  # To track visited nodes
    queue = deque([0])  # Queue initialized with starting node (0)
    bfs_order = []  # Stores the BFS traversal order

    visited[0] = True  # Mark starting node as visited

    while queue:
        node = queue.popleft()  # Dequeue front element
        bfs_order.append(node)  # Add to BFS result

        # Traverse all adjacent vertices of the current node
        for neighbor in adj[node]:
            if not visited[neighbor]:  # If not visited, enqueue it
                queue.append(neighbor)
                visited[neighbor] = True

    return bfs_order

# Example Test Cases
print(bfsOfGraph([[2,3,1], [0], [0,4], [0], [2]]))
# Expected Output: [0, 2, 3, 1, 4]

print(bfsOfGraph([[1, 2], [0, 2], [0, 1, 3, 4], [2], [2]]))
# Expected Output: [0, 1, 2, 3, 4]

print(bfsOfGraph([[1], [0, 2, 3], [1], [1, 4], [3]]))
# Expected Output: [0, 1, 2, 3, 4]

""" 
Time Complexity Analysis
Each node is enqueued once → O(V)
Each edge is traversed once → O(E)
Total Complexity: O(V + E)
Space Complexity
Visited array → O(V)
Queue storage → O(V) in the worst case
Total Space Complexity: O(V)
Final Thoughts
✅ Optimized BFS using a queue (deque for efficiency)
✅ Beginner-friendly explanation with comments
✅ Correct traversal order following adjacency list sequence
"""