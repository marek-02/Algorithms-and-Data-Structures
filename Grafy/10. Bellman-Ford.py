#najkrótsze ścieżki jeśli wagi mają być ujemne
#graf skierowany, działamy na krawędziach
#O(VE)

from math import inf
from turtle import goto

def relax(u, v, d, parent):
    if d[u[0]] > d[v] + u[1]:
        d[u[0]] = d[v] + u[1]
        parent[u[0]] = v



def BellmanFord(G, s):
    n = len(G)
    d = [inf for i in range(n)]
    d[s] = 0
    parent = [None for i in range(n)]
    for i in range(n - 1):
        for v in range(n):
            for u in G[v]:
                relax(u, v, d, parent)

    for v in range(n):
        for u in G[v]:
            if d[u[0]] > d[v] + u[1]: 
                print("Ujemny cykl")
    
    print(d)
    print(parent)

#powinien być graf skierowany, ten jest przekopiowany z przykładu z D
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
BellmanFord(G, 0)