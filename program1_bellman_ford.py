"""
Experiment 11: Advanced Graph Algorithms
Program 1: Bellman-Ford
Aim: Find shortest paths with negative edge weights and detect negative cycles.
"""

def bellman_ford(n, edges, source):
    dist = [float('inf')] * n
    dist[source] = 0
    for _ in range(n - 1):
        changed = False
        for u, v, w in edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                changed = True
        if not changed:
            break
    for u, v, w in edges:
        if dist[u] != float('inf') and dist[u] + w < dist[v]:
            return None, True
    return dist, False

edges = [(0, 1, 4), (0, 2, 5), (1, 2, -2), (2, 3, 3)]
print(bellman_ford(4, edges, 0))
