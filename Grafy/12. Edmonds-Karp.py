from queue import Queue


def BFS(G, s, t):
    n = len(G)
    parent = [-1 for i in range(n)]
    visited = [False for i in range(n)]
    visited[s] = True
    Q = Queue()
    Q.put(s)
    sciezka = []
    
    # for i in range(n):
    #     print(G[i])
    # print(s, t)
    
   
    while not Q.empty():
        u = Q.get()
        for v in range(n):
            if(G[u][v] > 0) and not visited[v]:
                visited[v] = True
                parent[v] = u
                if v == t: 
                    min_flow = G[parent[v]][v]
                    #print(min_flow, v, parent[v])
                    while parent[v] != -1:
                        # print("TU")
                        # print(parent, v)
                        sciezka.append(v)
                        if G[parent[v]][v] < min_flow:
                            min_flow = G[parent[v]][v]
                        v = parent[v]
                    sciezka.append(s)
                    sciezka.reverse()
                    print(sciezka, min_flow)
                    #for i in range(len(G)): print(G[i])
                    return sciezka, min_flow
                Q.put(v)
    return None, 0

def EdmondsKarp(G, s, t): #G to macierz nxn
    max_flow = 0
    sciezka, min_flow = BFS(G, s, t)
    while sciezka is not None:
        for i in range(len(sciezka) - 1):
            G[sciezka[i]][sciezka[i + 1]] -= min_flow
            G[sciezka[i + 1]][sciezka[i]] += min_flow
        for i in range(len(G)): print(G[i])
        max_flow += min_flow
        sciezka, min_flow = BFS(G, s, t)
    print("WYNIK:")
    print(max_flow)
    for i in range(len(G)): print(G[i])
    return max_flow


G = [
    [0, 4, 0, 3, 0, 0],
    [0, 0, 2, 2, 0, 0],
    [0, 0, 0, 0, 0, 4],
    [0, 2, 2, 0, 2, 0],
    [0, 0, 0, 0, 0, 5],
    [0, 0, 0, 0, 0, 0],
]

EdmondsKarp(G, 0, 5)