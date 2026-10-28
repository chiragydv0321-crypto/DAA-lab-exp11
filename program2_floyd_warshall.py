"""
Experiment 11: Advanced Graph Algorithms
Program 2: Floyd-Warshall
Aim: Compute all-pairs shortest paths using dynamic programming.
"""

def floyd_warshall(dist):
    d = [row[:] for row in dist]
    n = len(d)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if d[i][k] != float('inf') and d[k][j] != float('inf'):
                    d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return d

inf = float('inf')
g = [[0, 3, inf], [inf, 0, 1], [2, inf, 0]]
print(floyd_warshall(g))
