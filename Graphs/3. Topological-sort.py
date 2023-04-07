#sortowanie topologiczne skierowanego grafu bez cykli
#poniżej wersja listowa, wersja macierzowa analogiczna
tOut = 0

def DFS_lista_visit(G, u, visited, parent, timeOut, sortTop):
    global tOut
    visited[u] = True
    for v in G[u]:            
        if not visited[v]:
            parent[v] = u          
            DFS_lista_visit(G, v, visited, parent, timeOut, sortTop)
    sortTop.append(u)
    tOut += 1
    timeOut[u] = tOut

def sort_top(G):
    n = len(G)
    parent = [None for i in range(n)]
    visited = [False for i in range(n)]
    timeOut = [-1 for i in range(n)]
    sortTop = []

    for v in range(n):
        if not visited[v]:
            DFS_lista_visit(G, v, visited, parent, timeOut, sortTop)
    
    sortTop.reverse()

    print("\nSortowanie topologiczne:")
    for i in range(n):
        print(i, ": parent - ", parent[i], ", timeOut - ", timeOut[i])
    print(sortTop)

G = [
    [1, 2, 5],
    [2, 4],
    [],
    [],
    [3, 6],
    [4],
    []
]

sort_top(G)