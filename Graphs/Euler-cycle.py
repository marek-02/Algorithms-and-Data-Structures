#Cykl Eulera przechodzi wszystkie krawędzie dokładnie raz i wraca na początek 
#graf spójny nieskierowany posiada cykl Eulera wtw. gdy każdy jego wierzchołek ma parzysty stopień

def DFS_lista_visit(G, E, u, cykl):
    for v, e in G[u]:            
        if not E[e]:
            E[e] = True
            DFS_lista_visit(G, E, v, cykl)
    cykl.append(u)

def Cykl_Eulera(G, E):
    cykl = []
    DFS_lista_visit(G, E, 0, cykl)
    cykl.reverse()

    print(cykl)

#graf w postaci listowej, [numer wierzchołka, numer krawędzi] - potrzebne bo usuwamy krawędzie
G = [
    [[1, 0], [2, 1]],
    [[0, 0], [2, 2], [3, 3], [5, 4]],
    [[0, 1], [1, 2], [3, 5], [5, 6]],
    [[1, 3], [2, 5], [4, 7], [5, 8]],
    [[3, 7], [5, 9]],
    [[1, 4], [2, 6], [3, 8], [4, 9]]
]
E = [False for i in range(10)]

Cykl_Eulera(G, E)