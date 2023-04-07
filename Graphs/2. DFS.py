tIn = 0
tOut = 0

def DFS_macierz_visit(G, u, visited, parent, timeIn, timeOut):
    global tIn
    global tOut
    tIn += 1
    timeIn[u] = tIn
    visited[u] = True
    for v in range(len(G)):            
        if G[u][v] > 0 and not visited[v]:
            parent[v] = u          
            DFS_macierz_visit(G, v, visited, parent, timeIn, timeOut)
    tOut += 1
    timeOut[u] = tOut

def DFS_macierz(G, s):
    n = len(G)
    parent = [None for i in range(n)]
    visited = [False for i in range(n)]
    timeIn = [-1 for i in range(n)]
    timeOut = [-1 for i in range(n)]

    parent[s] = None
    DFS_macierz_visit(G, s, visited, parent, timeIn, timeOut)

    print("\nDFS macierzowy:")
    for i in range(n):
        print(i, ": parent - ", parent[i], ", timeIn - ", timeIn[i], ", timeOut - ", timeOut[i])

def DFS_lista_visit(G, u, visited, parent, timeIn, timeOut):
    global tIn
    global tOut
    tIn += 1
    timeIn[u] = tIn
    visited[u] = True
    for v in G[u]:            
        if not visited[v]:
            parent[v] = u          
            DFS_lista_visit(G, v, visited, parent, timeIn, timeOut)
    tOut += 1
    timeOut[u] = tOut

def DFS_lista(G, s):
    n = len(G)
    parent = [None for i in range(n)]
    visited = [False for i in range(n)]
    timeIn = [-1 for i in range(n)]
    timeOut = [-1 for i in range(n)]

    parent[s] = None
    DFS_lista_visit(G, s, visited, parent, timeIn, timeOut)

    print("\nDFS listowy:")
    for i in range(n):
        print(i, ": parent - ", parent[i], ", timeIn - ", timeIn[i], ", timeOut - ", timeOut[i])


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

#puszczać albo jeden, albo drugi bo obydwa korzystają ze zmiennych globalnych, więc by się nadpisały
#DFS_macierz(G_macierz, 0)
DFS_lista(G_lista, 0)