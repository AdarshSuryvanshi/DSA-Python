from collections import deque  # Import deque from collections module for efficient queue operations

def shortestPath(edges, N, M, src):
    # Create an adjacency list to store the graph connections
    adj = []  # Initialize an empty list for adjacency list representation
    for _ in range(N):  # Loop through the number of nodes
        adj.append([])  # Create an empty list for each node to store its neighbors
    
    for u, v in edges:  # Iterate through each edge pair
        adj[u].append(v)  # Add node v to the adjacency list of node u
        adj[v].append(u)  # Add node u to the adjacency list of node v (since the graph is undirected)
    
    # Print adjacency list for visualization
    print("Adjacency List Representation:")
    for i in range(N):  # Loop through each node
        print(f"Node {i}: {adj[i]}")  # Print the node and its connected neighbors
    
    # Distance array initialized to a large value (infinity) to indicate unvisited nodes
    dist = []  # Initialize an empty list to store distances
    for _ in range(N):  # Loop through each node
        dist.append(float('inf'))  # Set initial distance to infinity
    dist[src] = 0  # Set the source node's distance to 0 (starting point)
    
    # BFS queue initialization
    q = deque()  # Create a queue using deque for BFS traversal
    q.append(src)  # Add the source node to the queue
    
    while len(q) > 0:  # Continue BFS while the queue is not empty
        node = q.popleft()  # Remove and get the front node from the queue
        for neighbor in adj[node]:  # Iterate through all adjacent nodes of the current node
            if dist[node] + 1 < dist[neighbor]:  # If a shorter path to neighbor is found
                dist[neighbor] = dist[node] + 1  # Update the shortest distance to neighbor
                q.append(neighbor)  # Add the neighbor to the queue for further processing
    
    # Convert unreachable nodes to -1 (as per problem requirement)
    for i in range(N):  # Loop through each node
        if dist[i] == float('inf'):  # If the node's distance is still infinity, it means it's unreachable
            dist[i] = -1  # Mark it as -1
    
    return dist  # Return the final shortest path distances

# User input section
N = int(input("Enter number of nodes: "))  # Take input for number of nodes in the graph
M = int(input("Enter number of edges: "))  # Take input for number of edges in the graph
edges = []  # Initialize an empty list to store edge pairs
print("Enter edges:")  # Prompt user to input edges
for _ in range(M):  # Loop through the number of edges
    u, v = map(int, input().split())  # Read two space-separated integers representing an edge
    edges.append([u, v])  # Store the edge in the edges list

src = int(input("Enter source node: "))  # Take input for the source node
print(shortestPath(edges, N, M, src))  # Call the function and print the result


"""
 9
Enter number of edges: 10
Enter edges:
0 1
0 3
3 4
4 5
5 6
1 2
2 6
6 7
7 8
6 8
Enter source node: 0
Adjacency List Representation:
Node 0: [1, 3]
Node 1: [0, 2]
Node 2: [1, 6]
Node 3: [0, 4]
Node 4: [3, 5]
Node 5: [4, 6]
Node 6: [5, 2, 7, 8]
Node 7: [6, 8]
Node 8: [7, 6]
[0, 1, 2, 1, 2, 3, 3, 4, 4]
"""