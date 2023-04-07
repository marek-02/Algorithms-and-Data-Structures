#O(E logV)
#wagi nieujemne
from math import inf
from queue import PriorityQueue

#tu przykład na listach (u, d(v, u)), ogólnie jeden pies
# def relax(u, v, d, parent):
#     if d[u[0]] > d[v] + u[1]:
#         d[u[0]] = d[v] + u[1]
#         parent[u] = v
    

def Dijkstra(G, s):
    n = len(G)
    d = [inf for _ in range(n)]
    d[s] = 0
    parent = [None for i in range(n)]
    visited = [False for i in range(n)]
    pq = PriorityQueue()
    pq.put((d[s], s))

    while not pq.empty():
        dist, v = pq.get()
        if visited[v]: continue
        visited[v] = True
        for u in G[v]:
            if not visited[u[0]]:
                if d[u[0]] > d[v] + u[1]:
                    d[u[0]] = d[v] + u[1]
                    parent[u[0]] = v
                    pq.put((d[u[0]], u[0]))
    print(d)
    print(parent)

G = [
    [(1, 1), (7, 2)],
    [(2, 2), (4, 3), (0, 1)],
    [(1, 2), (3, 5)],
    [(2, 5), (6, 1)],
    [(1, 3), (7, 1), (5, 3)],
    [(4, 3), (8, 1), (6, 8)],
    [(3, 1), (5, 8), (8, 4)],
    [(0, 2), (4, 1), (8, 7)],
    [(7, 7), (6, 4), (5, 1)],
]
Dijkstra(G, 0)