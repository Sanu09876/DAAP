INF = float('inf')  # Define INF as infinity

def floyd_warshall(dist, n):
    # Floyd-Warshall algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    # Printing the result matrix
    print("\nThe following matrix shows the minimum costs between every pair of cities:")
    for i in range(n):
        for j in range(n):
            if dist[i][j] == INF:
                print("INF", end="\t")
            else:
                print(dist[i][j], end="\t")
        print()  # New line after each row

def main():
    # Input number of cities
    n = int(input("Enter the number of cities: "))
    
    # Initialize the distance matrix
    dist = []
    
    print("\nEnter the cost matrix (use 'INF' for no direct connection):")
    print("Enter the matrix row by row:")
    
    # Input the matrix
    for i in range(n):
        row = input().split()
        row = [INF if x == 'INF' else int(x) for x in row]
        dist.append(row)
    
    # Apply the Floyd-Warshall algorithm
    floyd_warshall(dist, n)

if __name__ == "__main__":
    main()

