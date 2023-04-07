#dla grafu skierowanego, u, v należą do silnie spójnej składowej jak jest śćieżka skierowana z u do v i z v do u

def DFS_macierz_visit(G, u, visited, przetworzone):
    visited[u] = True
    for v in range(len(G)):            
        if G[u][v] > 0 and not visited[v]:
            DFS_macierz_visit(G, v, visited, przetworzone)
    przetworzone.append(u)

def DFS_ustaw_skladowa(G, u, visited, skladowe):
    visited[u] = True
    for v in range(len(G)): #G[v][u] bo odwrocone krawedzie
        if G[v][u] > 0 and not visited[v]:
            skladowe[v] = skladowe[u]
            DFS_ustaw_skladowa(G, v, visited, skladowe)

def spojne_skl(G):
    n = len(G)
    visited = [False for i in range(n)]
    przetworzone = []
    skladowe = [i for i in range(n)]

    for v in range(n):
        if not visited[v]:
            DFS_macierz_visit(G, v, visited, przetworzone)
    
    przetworzone.reverse()
    visited = [False for i in range(n)]

    for v in przetworzone:
        if not visited[v]:
            DFS_ustaw_skladowa(G, v, visited, skladowe)

    print(przetworzone)
    print(skladowe)


G = [
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0]
]

spojne_skl(G)