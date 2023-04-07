#mostem w spojnym grafie nieskierowanym jest krawedz której usunięcie rozspójnia graf
#e jest mostem wtw. gdy nie leży na żadnym cyklu

tIn = 0

def DFS_lista_visit(G, u, visited, parent, timeIn, low):
    global tIn
    tIn += 1
    timeIn[u] = tIn
    low[u] = tIn
    visited[u] = True
    for v in G[u]:            
        if not visited[v]:
            parent[v] = u 
            DFS_lista_visit(G, v, visited, parent, timeIn, low)
            if low[v] < low[u]:
                low[u] = low[v]
        elif parent[u] != v and timeIn[v] < low[u]:
            low[u] = timeIn[v]        
    
def mosty(G): #zakładamy że graf spójny, inaczej bez sensu
    n = len(G)
    parent = [None for i in range(n)]
    visited = [False for i in range(n)]
    timeIn = [-1 for i in range(n)]
    low = [-1 for i in range(n)]
    

    for u in range(n):
        if not visited[u]:
            DFS_lista_visit(G, u, visited, parent, timeIn, low)


    for i in range(n):
        print(i, parent[i], low[i], timeIn[i])


    print("\nMosty w grafe G:")
    for v in range(n):
        if timeIn[v] == low[v] and parent[v] is not None:
            print('\n', v, parent[v])

G = [
    [1, 6],
    [0, 2],
    [1, 3, 6],
    [2, 5, 4],
    [3, 5],
    [3, 4],
    [0, 2, 7],
    [6]
]

mosty(G)