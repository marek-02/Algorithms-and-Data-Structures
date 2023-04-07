from queue import Queue

def BFS_macierz(G, s):
    n = len(G)
    Q = Queue()
    parent = [None for i in range(n)]
    visited = [False for i in range(n)]
    d = [-1 for i in range(n)]

    parent[s] = None
    visited[s] = True
    d[s] = 0
    Q.put(s)

    while not Q.empty():
        u = Q.get()
        for v in range(n):
            if G[u][v] > 0 and not visited[v]:
                visited[v] = True
                d[v] = d[u] + 1
                parent[v] = u
                Q.put(v)
    print("\nBFS macierzowy:")
    for i in range(n):
        print(i, ": parent - ", parent[i], ", odleglosc - ", d[i])

def BFS_lista(G, s):
    n = len(G)
    Q = Queue()
    parent = [None for i in range(n)]
    visited = [False for i in range(n)]
    d = [-1 for i in range(n)]

    parent[s] = None
    visited[s] = True
    d[s] = 0
    Q.put(s)

    while not Q.empty():
        u = Q.get()
        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                d[v] = d[u] + 1
                parent[v] = u
                Q.put(v)
    print("\nBFS listowy:")
    for i in range(n):
        print(i, ": parent - ", parent[i], ", odleglosc - ", d[i])


G_macierz = [
    [0, 1, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 0, 0],
    [1, 0, 0, 1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 1, 0]
]

G_lista = [
    [1, 2],
    [0, 4],
    [0, 3, 5],
    [2, 4],
    [1, 3, 5],
    [2, 4, 6],
    [5, 7],
    [6],
]

BFS_macierz(G_macierz, 0)
BFS_lista(G_lista, 0)