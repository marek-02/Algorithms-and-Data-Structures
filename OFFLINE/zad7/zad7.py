from zad7testy import runtests

def DFSVisit(G, u, index, visited, parent):
    visited[u] = True
    #print(u, index, visited, parent)
    czyWszedl = False
    for v in G[u][index]:
        if not visited[v]:
            czyWszedl = True
            parent[v] = u
            if u in G[v][0]: index = 1
            else: index = 0
            #DFSVisit(G, v, index, visited, parent)
            wynik = DFSVisit(G, v, index, visited, parent)
            if wynik is not None: return wynik
        if not czyWszedl:
            if 0 in G[u][index] and not False in visited: 
                wynik = [0, u]
                while parent[u] != 0:
                    wynik.append(parent[u])
                    u = parent[u]
                #print("GIT", wynik)
                return wynik
    visited[u] = False
    return None

def DFS(G):
    n = len(G)
    parent = [-1 for i in range(n)]
    visited = [False for i in range(n)]
    visited[0] = True

    v, index = 0, 0

    for u in G[v][index]:
        if not visited[u]:
            parent[u] = v
            if v in G[u][0]: index = 1
            else: index = 0
            wynik = DFSVisit(G, u, index, visited, parent)
            if wynik is not None: return wynik
    return wynik
    #print(visited, parent)


def droga(G):

    return DFS(G)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( droga, all_tests = True )
# G = [([1], [3]),
#      ([0], [3, 2]),
#      ([3], [1]),
#      ([0, 1], [2])]

# print(DFS(G))