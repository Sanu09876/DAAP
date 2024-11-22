import heapq
from collections import defaultdict

def networkDelayTime(times, N, K):
    graph = defaultdict(list)  # adjacency list for graph
    
    # Build the graph
    for u, v, w in times:
        graph[u].append((v, w))
    
    # Min-heap to store (time, node)
    min_heap = [(0, K)]
    
    # Dictionary to store shortest time to each node
    shortest_time = {}
    
    # Dijkstra's algorithm
    while min_heap:
        time, node = heapq.heappop(min_heap)
        
        # If node is already visited, skip
        if node in shortest_time:
            continue
        
        # Mark the node with its time
        shortest_time[node] = time
        
        # Traverse neighbors
        for neighbor, t in graph[node]:
            if neighbor not in shortest_time:
                heapq.heappush(min_heap, (time + t, neighbor))
    
    # Check if all nodes are reached
    if len(shortest_time) == N:
        return max(shortest_time.values())
    else:
        return -1

# User input
N = int(input("Enter the number of nodes (N): "))  # Number of nodes
M = int(input("Enter the number of edges (M): "))  # Number of edges
times = []

print("Enter the edges in the format: 'u v w' where u -> v with weight w")
for i in range(M):
    u, v, w = map(int, input(f"Edge {i+1}: ").split())
    times.append([u, v, w])

K = int(input("Enter the starting node (K): "))  # Starting node (K)

# Call the function and output the result
result = networkDelayTime(times, N, K)
print(f"The time it takes for the signal to reach all nodes is: {result}")

