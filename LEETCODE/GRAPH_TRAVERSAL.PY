from collections import deque

# Graph class to represent a graph using an adjacency list
class Graph:
    def __init__(self, vertices):
        """
        Initialize a graph with given number of vertices.
        :param vertices: The number of vertices in the graph.
        """
        self.V = vertices  # Number of vertices
        self.graph = [[] for _ in range(vertices)]  # Adjacency list to store the graph

    def add_edge(self, u, v):
        """
        Add an edge between vertices u and v.
        :param u: Starting vertex of the edge.
        :param v: Ending vertex of the edge.
        """
        self.graph[u].append(v)  # Add v to the adjacency list of u.

    # 1) Depth-First Search (DFS)
    def dfs(self, start):
        """
        Perform Depth-First Search starting from the given node.
        :param start: The node to start DFS from.
        """
        visited = [False] * self.V  # List to keep track of visited nodes.
        self._dfs_recursive(start, visited)  # Call the recursive DFS helper function.

    def _dfs_recursive(self, node, visited):
        """
        Helper function to perform DFS recursively.
        :param node: The current node being visited.
        :param visited: List to keep track of visited nodes.
        """
        visited[node] = True  # Mark the current node as visited.
        print(node, end=" -> ")  # Print the current node.
        
        # Recur for all the vertices adjacent to the current vertex.
        for neighbor in self.graph[node]:
            if not visited[neighbor]:
                self._dfs_recursive(neighbor, visited)

    # 2) Breadth-First Search (BFS)
    def bfs(self, start):
        """
        Perform Breadth-First Search starting from the given node.
        :param start: The node to start BFS from.
        """
        visited = [False] * self.V  # List to keep track of visited nodes.
        queue = deque([start])  # Use a queue for BFS.
        visited[start] = True  # Mark the starting node as visited.

        while queue:
            node = queue.popleft()  # Pop from the front of the queue.
            print(node, end=" -> ")  # Print the current node.
            
            # Visit all the unvisited adjacent vertices and enqueue them.
            for neighbor in self.graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)

    # 3) Topological Sort (for Directed Acyclic Graphs - DAG)
    def topological_sort(self):
        """
        Perform Topological Sort on the graph.
        This is valid only for Directed Acyclic Graphs (DAGs).
        """
        visited = [False] * self.V  # List to keep track of visited nodes.
        stack = []  # Stack to store the topological order.

        # Call the recursive helper function for each unvisited node.
        for i in range(self.V):
            if not visited[i]:
                self._topological_sort_helper(i, visited, stack)

        # Print the topological order.
        print("Topological Sort: ", end="")
        while stack:
            print(stack.pop(), end=" -> ")  # Print nodes in reverse order of their finishing times.

    def _topological_sort_helper(self, node, visited, stack):
        """
        Helper function to perform DFS and store the topological order.
        :param node: The current node being visited.
        :param visited: List to keep track of visited nodes.
        :param stack: The stack that stores the topological order.
        """
        visited[node] = True  # Mark the current node as visited.

        # Recur for all the vertices adjacent to the current vertex.
        for neighbor in self.graph[node]:
            if not visited[neighbor]:
                self._topological_sort_helper(neighbor, visited, stack)
        
        # Push the node to the stack after visiting all its neighbors.
        stack.append(node)

# Create a graph and test the traversal techniques
if __name__ == "__main__":
    g = Graph(6)  # Initialize a graph with 6 vertices

    # Add edges to the graph
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.add_edge(2, 4)
    g.add_edge(3, 5)
    g.add_edge(4, 5)

    print("DFS Traversal starting from node 0:")
    g.dfs(0)  # Perform DFS starting from node 0
    print("\n")

    print("BFS Traversal starting from node 0:")
    g.bfs(0)  # Perform BFS starting from node 0
    print("\n")

    print("Topological Sort of the graph:")
    g.topological_sort()  # Perform Topological Sort
