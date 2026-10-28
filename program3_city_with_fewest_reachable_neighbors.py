"""
Experiment 11: Advanced Graph Algorithms
Program 3: City with Fewest Reachable Neighbors
Aim: Find the city with the fewest neighbors within a distance threshold.
"""

def city_fewest_neighbors(n, edges, threshold):
    inf = float('inf')
    d = [[inf] * n for _ in range(n)]
    for i in range(n):
        d[i][i] = 0
    for u, v, w in edges:
        d[u][v] = d[v][u] = min(d[u][v], w)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    counts = [sum(1 for j in range(n) if j != i and d[i][j] <= threshold) for i in range(n)]
    return max(range(n), key=lambda i: (-counts[i], i))

print(city_fewest_neighbors(4, [(0, 1, 3), (1, 2, 1), (2, 3, 1), (0, 3, 4)], 4))
