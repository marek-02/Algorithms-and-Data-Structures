from math import inf

def Dijkstra(G, s):
    n = len(G)

    dist = [inf for _ in range(n)]
    parent = [-1 for _ in range(n)]
    visited = [False for _ in range(n)]
    
    dist[s] = 0

    for _ in range(n):
        minimum = inf
        u = -1
        for i in range(n):
            if dist[i] < minimum and not visited[i]:
                minimum = dist[i]
                u = i
        visited[u] = True
        for i in range(n):
            if G[u][i] != 0 and not visited[i]:
                if dist[u] + G[u][i] < dist[i]:
                    dist[i] = dist[u] + G[u][i]
                    parent[i] = u

    
    print(dist)
    print(parent)

G = [
    [0, 1, 0, 0, 0, 0, 0, 2, 0],
    [1, 0, 2, 0, 3, 0, 0, 0, 0],
    [0, 2, 0, 5, 0, 0, 0, 0, 0],
    [0, 0, 5, 0, 0, 0, 1, 0, 0],
    [0, 3, 0, 0, 0, 3, 0, 1, 0],
    [0, 0, 0, 0, 3, 0, 8, 0, 1],
    [0, 0, 0, 1, 0, 8, 0, 0, 4],
    [2, 0, 0, 0, 1, 0, 0, 0, 7],
    [0, 0, 0, 0, 0, 1, 4, 7, 0],
]
Dijkstra(G, 0)