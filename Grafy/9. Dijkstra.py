#O(E logV)
#wagi nieujemne
from math import inf
from queue import PriorityQueue

#tu przykład na listach (u, d(v, u)), ogólnie jeden pies
def relax(u, v, d, parent):
    if d[u[0]] > d[v] + u[1]:
        d[u[0]] = d[v] + u[1]
        parent[u] = v
    

def Dijkstra(G, s):
    n = len(G)
    d = [int for i in range(n)]
    d[s] = 0
    parent = [None for i in range(n)]
    visited = [False for i in range(n)]
    pq = PriorityQueue()
    pq.put(d[s], s)

    while not pq.empty():
        d, v = pq.get()
        visited[v] = True
        for u in G[v]:
            if not visited[u]:
                relax(u, v, d, parent)
                pq.put(d[u[0]], u[1])