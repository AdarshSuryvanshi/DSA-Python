""" 
Graph and Vertices - Python Implementation
Concept: Counting Undirected Graphs
A graph is a collection of vertices (nodes) and edges (connections between nodes).
For n vertices, each pair of vertices can either have an edge or not, meaning each pair has 2 choices (edge exists or not).

Key Points:
Total possible edges in an undirected graph with n vertices = C(n, 2) = (n * (n - 1)) / 2
Because each edge connects two nodes.
Each edge can either exist or not exist, so for E edges, the total number of possible graphs is 2^E.
Formula:
Total graphs 
"""
# Graph and Vertices - Counting Number of Undirected Graphs
# ------------------------------------------------------------
# Given `n` vertices, the number of possible undirected graphs is:
# 2^(n * (n - 1) / 2), since each pair of nodes can either be connected or not.
# ------------------------------------------------------------

def countGraphs(n):
    """
    Function to calculate the number of undirected graphs possible with 'n' vertices.
    
    :param n: Number of vertices
    :return: Number of possible graphs
    """
    # Step 1: Calculate number of possible edges
    edges = (n * (n - 1)) // 2  # Total possible edges in an undirected graph
    
    # Step 2: Calculate total graphs (Each edge can either exist or not => 2^edges)
    return 2 ** edges  # Using exponentiation to find the total graphs

# Example Test Cases
print(countGraphs(2))  # Output: 2
print(countGraphs(5))  # Output: 1024

#-------------------------------------------------------------------------------------------------------------------------------------------------------
""" 
ime Complexity Analysis
Formula Calculation: 
𝑂
(
1
)
O(1)
Exponentiation (2^E): Python handles it efficiently, O(1) for small n
(For very large n, it may take more time due to large number calculations).
Space Complexity
O(1) (Only a few variables are used)
Final Thoughts
✅ Optimized approach with direct formula calculation.
✅ Beginner-friendly with clear logic and explanation.
✅ Uses Python’s exponentiation for quick computation.
"""