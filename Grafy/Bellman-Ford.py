#najkrótsze ścieżki jeśli wagi mają być ujemne
#graf skierowany, działamy na krawędziach
#O(VE)

from math import inf

def relax(u, v, d, parent):
    if d[u[0]] > d[v] + u[1]:
        d[u[0]] = d[v] + u[1]
        parent[u] = v



def BellmanFord(G, s):
    n = len(G)
    d = [inf for i in range(n)]
    d[s] = 0
    parent = [None for i in range(n)]
    #itd..