class Node:
    def __init__(self, val):
        self.parent = self
        self.val = val
        self.rank = 0

def find(x):
    if x.parent != x:
        x.parent = find(x.parent)
    return x.parent

def union(x, y):
    x = find(x)
    y = find(y)
    if x == y: return
    if x.rank > y.rank: 
        y.parent = x
    else: 
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1

def makeset(v):
    return Node(v)


def Kruskal(G):
    n = len(G)
    E = []
    for i in range(G):
        for j in range(G[i]):
            if (G[i][j][0], i, G[j][i]) not in E:
                E.append(i, G[i][j][0], G[i][j][1])
    E.sort(key = lambda x: x[2])
    V = [makeset(v) for v in range(n)]
    e = len(E)
    MST = []
    for e in E:
        u, v = e[0], e[1]
        if find(u) != find(v):
            union(V[u], V[v])
            MST.append(e)
    return MST
