import heapq  # Import heapq module to use priority queue

def dijkstra(V, adj, S):
    """
    Function to find the shortest distance from source vertex S to all vertices.
    :param V: Number of vertices in the graph
    :param adj: Adjacency list representation of the graph
    :param S: Source vertex
    :return: List of shortest distances from source to all vertices
    """
    
    # Priority queue (min-heap) to store (distance, node) pairs
    pq = []  # Initialize an empty list for priority queue
    
    # Distance array initialized to a large value (infinity) for all nodes
    distTo = []  # Create an empty list to store shortest distances
    for i in range(V):  # Loop through all vertices
        distTo.append(float('inf'))  # Set initial distance to infinity
    
    # Distance of the source node from itself is always 0
    distTo[S] = 0  # Set source node's distance to 0
    
    # Push the source node into the priority queue
    heapq.heappush(pq, (0, S))  # Insert (distance 0, source node) into min-heap
    
    while len(pq) > 0:  # Continue while priority queue is not empty
        
        # Extract the node with the smallest distance
        dis, node = heapq.heappop(pq)  # Pop element with the smallest distance
        
        # Iterate over all adjacent nodes of the current node
        for neighbor in adj[node]:  # Loop through neighbors of the current node
            v = neighbor[0]  # Extract the adjacent node
            w = neighbor[1]  # Extract the weight of the edge
            
            # If the new calculated distance is smaller than the previously stored distance
            if dis + w < distTo[v]:  
                distTo[v] = dis + w  # Update the shortest distance to v
                
                # Push the updated distance to the priority queue
                heapq.heappush(pq, (distTo[v], v))
    
    return distTo  # Return the list of shortest distances

# Driver code
V = int(input("Enter number of vertices: "))  # Take input for number of vertices
E = int(input("Enter number of edges: "))  # Take input for number of edges
adj = []  # Initialize an empty adjacency list

# Create an empty list for each vertex
for i in range(V):  # Loop through number of vertices
    adj.append([])  # Append an empty list for each vertex

print("Enter edges in format: u v w (where u and v are nodes, and w is weight)")
for i in range(E):  # Loop through number of edges
    u, v, w = map(int, input().split())  # Read space-separated integers u, v, and w
    adj[u].append([v, w])  # Add edge u -> v with weight w
    adj[v].append([u, w])  # Add edge v -> u with weight w (for undirected graph)

S = int(input("Enter source node: "))  # Take input for source node
result = dijkstra(V, adj, S)  # Call Dijkstra function

print("Shortest distances from source:")
for i in range(V):  # Loop through each vertex
    print(f"Node {i}: {result[i]}")  # Print shortest distance to each node

"""
Enter number of vertices: 6
Enter number of edges:
 8
Enter edges in format: u v w (where u and v are nodes, and w is weight)
0 1 4
0 2 4
1 2 2
2 3 3
2 5 6
2 4 1
4 5 3
3 5 2
Enter source node: 0
Shortest distances from source:
Node 0: 0
Node 1: 4
Node 2: 4
Node 3: 7
Node 4: 5
Node 5: 8
"""