from queue import PriorityQueue
from math import inf

#tu przykład na listach (u, d(v, u)), ogólnie jeden pies
def Prime(G, s):
    n = len(G)
    parent = [None for i in range(n)]
    visited = [False for i in range(n)]
    d = [inf for i in range(n)]
    d[s] = 0
    pq = PriorityQueue()
    pq.put(d[s], s)

    while not pq.empty():
        d, v = pq.get()
        visited[v] = True
        for u in G[v]:
            if not visited[u[0]] and d[u[0]] > u[1]:
                parent[u[0]] = v
                pq.put(d[u[0]], u[1])
    MST = []
    for i in range(n):
        if parent[i] is not None:
            MST.append(i, parent[i], d[i])
    
    return MST
