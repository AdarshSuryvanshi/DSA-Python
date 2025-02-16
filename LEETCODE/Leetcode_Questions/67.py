""" 
Depth-First Search (DFS) - Python Implementation
Concept: Depth-First Search (DFS) Traversal of a Graph
Depth-First Search (DFS) is a traversal algorithm for graphs:

Uses recursion (or a stack) to explore as deep as possible before backtracking.
Starts from vertex 0 and explores its adjacent vertices before moving to other unvisited nodes.
Ensures that each node is visited only once using a visited list.
Key Points:
Uses recursion for DFS traversal.
Time Complexity: O(V + E) (Each vertex and edge is visited once).
Space Complexity: O(V) (Recursive call stack + visited nodes).
Ensures traversal order follows adjacency list sequence.

"""
# --------------------------------------------------------
# Depth-First Search (DFS) of a Graph
# --------------------------------------------------------
# Given an adjacency list `adj`, perform DFS traversal starting from node 0.
# --------------------------------------------------------

def dfsOfGraph(adj):
    """
    Function to perform DFS traversal on a given adjacency list representation of a graph.

    :param adj: List of lists representing the adjacency list
    :return: List containing DFS traversal order
    """
    V = len(adj)  # Number of vertices
    visited = [False] * V  # To track visited nodes
    dfs_order = []  # Stores the DFS traversal order

    def dfs(node):
        """Recursive DFS function"""
        visited[node] = True  # Mark the node as visited
        dfs_order.append(node)  # Add node to DFS result

        # Traverse all adjacent vertices of the current node
        for neighbor in adj[node]:
            if not visited[neighbor]:  # If not visited, call DFS recursively
                dfs(neighbor)

    dfs(0)  # Start DFS from node 0
    return dfs_order

# Example Test Cases
print(dfsOfGraph([[2,3,1], [0], [0,4], [0], [2]]))
# Expected Output: [0, 2, 4, 3, 1]

print(dfsOfGraph([[1, 2], [0, 2], [0, 1, 3, 4], [2], [2]]))
# Expected Output: [0, 1, 2, 3, 4]
""" 
Time Complexity Analysis
Each node is visited once → O(V)
Each edge is traversed once → O(E)
Total Complexity: O(V + E)
Space Complexity
Visited array → O(V)
Recursive call stack → O(V) in worst case (linear recursion depth for deep trees)
Total Space Complexity: O(V)
Final Thoughts
✅ Optimized DFS using recursion
✅ Beginner-friendly explanation with comments
✅ Correct traversal order following adjacency list sequence


"""