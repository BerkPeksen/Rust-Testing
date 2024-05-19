import sys

import time

start_time = time.time()
V = 10  # Number of vertices in the graph

def tsp(graph, mask, pos):
    visited_all = (1 << V) - 1
    if mask == visited_all:
        return graph[pos][0]  # Return to starting city

    min_cost = sys.maxsize

    for city in range(V):
        if (mask & (1 << city)) == 0:  # If city not visited
            new_cost = graph[pos][city] + tsp(graph, mask | (1 << city), city)
            min_cost = min(min_cost, new_cost)

    return min_cost

if __name__ == "__main__":
    graph = [
        [0, 29, 20, 21, 16, 31, 100, 12, 4, 31],
        [29, 0, 15, 29, 28, 40, 72, 21, 29, 41],
        [20, 15, 0, 15, 14, 25, 81, 9, 23, 27],
        [21, 29, 15, 0, 4, 12, 92, 12, 25, 13],
        [16, 28, 14, 4, 0, 16, 94, 9, 20, 16],
        [31, 40, 25, 12, 16, 0, 95, 24, 36, 3],
        [100, 72, 81, 92, 94, 95, 0, 90, 101, 99],
        [12, 21, 9, 12, 9, 24, 90, 0, 15, 25],
        [4, 29, 23, 25, 20, 36, 101, 15, 0, 35],
        [31, 41, 27, 13, 16, 3, 99, 25, 35, 0]
    ]

    start_city = 0  # Starting city is 0
    mask = 1 << start_city  # Mark start city as visited

    min_path_cost = tsp(graph, mask, start_city)

    print("Minimum path cost:", min_path_cost)
    elapsed_time = (time.time() - start_time) * 1000  # Convert to milliseconds
    print(f"Time taken: {elapsed_time:.3f} milliseconds")   
    
