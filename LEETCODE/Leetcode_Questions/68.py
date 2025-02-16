""" 
Topological Sorting of a Directed Acyclic Graph (DAG)
Topological sorting is a linear ordering of vertices such that for every directed edge u → v, vertex u appears before v in the ordering.
Key Condition: Only applicable to Directed Acyclic Graphs (DAGs) (Graphs without cycles).

Approaches to Solve Topological Sort
There are two standard algorithms to compute a topological ordering:

Kahn’s Algorithm (BFS-based, uses in-degree tracking).
DFS-based Algorithm (uses recursion and stack).
Approach 1: Kahn's Algorithm (BFS)
Uses a queue and in-degree array (number of incoming edges for each node).
Steps:
Compute in-degree for each vertex.
Push all vertices with in-degree 0 into a queue.
Remove nodes from the queue, add them to result, and decrease in-degree of adjacent nodes.
Repeat until the queue is empty.
Python Code (Using Kahn's Algorithm - BFS)

"""
## Approach 1 :- Kahn Algo Topo-Sort by (BFS)
from collections import deque

def topologicalSort(V, adj):
    """
    Function to return a topological sort of the given DAG using Kahn's Algorithm (BFS).

    :param V: Number of vertices
    :param adj: Adjacency list representation of graph
    :return: List containing a valid topological sort order
    """
    in_degree = [0] * V  # Step 1: Compute in-degree of each vertex
    for u in range(V):
        for v in adj[u]:
            in_degree[v] += 1

    # Step 2: Push nodes with in-degree 0 into the queue
    queue = deque([i for i in range(V) if in_degree[i] == 0])
    topo_order = []

    while queue:
        node = queue.popleft()
        topo_order.append(node)

        # Step 3: Reduce in-degree of adjacent vertices
        for neighbor in adj[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:  # If in-degree becomes 0, add to queue
                queue.append(neighbor)

    return topo_order if len(topo_order) == V else []  # Return empty list if cycle exists

# Example Test Cases
print(topologicalSort(4, [[], [0], [0], [0]]))  
# Possible Output: [3, 2, 1, 0] or any valid order

print(topologicalSort(6, [[], [3], [3], [], [0,1], [0,2]]))  
# Possible Output: [4, 5, 0, 1, 2, 3] or any valid order

#-------------------------------------------------------------------------------------------------------------------------------------------------------
""" 

Approach 2: DFS-Based (Using Stack)
Uses recursion and a stack to maintain order.
Steps:
Visit unvisited nodes using DFS recursion.
Once a node has no more children to explore, push it onto a stack.
Pop elements from the stack to get the topological order.

"""
def topologicalSortDFS(V, adj):
    """
    Function to return a topological sort of the given DAG using DFS.

    :param V: Number of vertices
    :param adj: Adjacency list representation of graph
    :return: List containing a valid topological sort order
    """
    visited = [False] * V
    stack = []

    def dfs(node):
        """Recursive DFS function"""
        visited[node] = True
        for neighbor in adj[node]:
            if not visited[neighbor]:
                dfs(neighbor)
        stack.append(node)  # Push node after visiting all its children

    for i in range(V):
        if not visited[i]:  # Run DFS for unvisited nodes
            dfs(i)

    return stack[::-1]  # Reverse stack to get correct topological order

# Example Test Cases
print(topologicalSortDFS(4, [[], [0], [0], [0]]))  
# Possible Output: [3, 2, 1, 0] or any valid order

print(topologicalSortDFS(6, [[], [3], [3], [], [0,1], [0,2]]))  
# Possible Output: [4, 5, 0, 1, 2, 3] or any valid order

""" 
Complexity Analysis
Algorithm	Time Complexity	Space Complexity
Kahn’s BFS	O(V + E)	O(V)
DFS-based	O(V + E)	O(V)
Explanation:

O(V + E) for adjacency list traversal.
O(V) for queue (BFS) or recursive stack (DFS).
Final Thoughts
✅ Both algorithms work efficiently for DAGs
✅ Kahn’s Algorithm (BFS) is easier to understand & iterative
✅ DFS-based method is recursive & stack-based
✅ Both return valid topological orders


"""
