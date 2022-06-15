#najkrótsze ścieżki jeśli wagi mają być ujemne
#graf skierowany, działamy na krawędziach
#wersja macierzowa, jak nie ma krawędzi to None
#O(VE)

from math import inf

def relax(u, v, d, parent, uvD):
    if d[u] > d[v] + uvD:
        d[u] = d[v] + uvD
        parent[u] = v



def BellmanFord(G, s):
    n = len(G)
    d = [inf for i in range(n)]
    d[s] = 0
    parent = [None for i in range(n)]
    E = []

    for i in range(G):
        for j in range(G):
            if G[i][j] != None and (j, i, G[i][j]) not in E:
                E.append(i, j, G[i][j])
    
    for i in range(n):
        for j in range(len(E)):
            relax(E[j][0], E[j][1], d, parent, E[j][2])

#sprawdzenie czy nie ma ujemnego cyklu
    for e in E:
        if d[e[1]] > d[e[0]] + G[e[0]][e[1]]:
            return False
    return True