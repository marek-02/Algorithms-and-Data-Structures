#reprezentacja macierzowa, odległości między każdą parą wierzchołków

def FloydWarshall(G):
    n = len(G)
    
    for i in range(n):
        print(G[i])
    for k in range(n):
        for u in range(n):
            for v in range(n):
                if G[u][k] > 0 and G[k][v] > 0 and u != v:
                    #print(u, v, k)
                    G[u][v] = min(G[u][v], G[u][k] + G[k][v])
    print("\npo algorytmie:")
    for i in range(n):
        print(G[i])


G = [
    [0, 1, 0, 0],
    [1, 0, 3, 7],
    [0, 3, 0, 2],
    [0, 7, 2, 0],
]

FloydWarshall(G)