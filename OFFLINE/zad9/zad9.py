from queue import Queue
from zad9testy import runtests

def reverse(T):
    n = len(T)
    for i in range(n // 2):
        T[i], T[n - 1 - i] = T[n - 1 - i], T[i]

def BFS(C, F, s, t):
    n = len(C)
    parent = [-1 for i in range(n)]
    Q = Queue()
    Q.put(s)
    sciezka = []

    
    while not Q.empty():
        u = Q.get()
        for v in range(n):
            if(C[u][v] > F[u][v]):
                if parent[v] == -1: parent[v] = u
                if v == t: 
                    while v != -1:
                        sciezka.append(v)
                        v = parent[v]
                    reverse(sciezka)
                    return sciezka
                Q.put(v)
    
    return None

def maxflow(G, s):
    n = 0
    for kr in G:
        if kr[0] > n: n = kr[0]
        if kr[1] > n: n = kr[1]
    n += 1
    C = [[0 for i in range(n + 1)] for j in range(n + 1)]
    #F = [[0 for i in range(n + 1)] for j in range(n + 1)]
    t = n

    for kr in G:
        C[kr[0]][kr[1]] = kr[2]
    m_flow = 0
    for i in range(n): m_flow += C[s][i]

    #print("C:\n", C, '\n\n\n')
    wynik = 0
    for i in range(n):    
        for j in range(i + 1, n):
            F = [[0 for i in range(n + 1)] for j in range(n + 1)]    
            for x in range(n + 1):
                C[x][t] = 0            
            C[i][t] = m_flow
            C[j][t] = m_flow
            sciezka = BFS(C, F, s, t)
            while sciezka is not None:
                #print(sciezka, F, C)
                l = len(sciezka) - 1
                flow = min(C[sciezka[k]][sciezka[k + 1]] - F[sciezka[k]][sciezka[k + 1]] for k in range(l))
                for k in range(l):
                    F[sciezka[k]][sciezka[k + 1]] += flow
                    F[sciezka[k + 1]][sciezka[k]] += flow
                #if i == 4 and j == 5:
                    #print(sciezka, "\nF:\n", F)
                sciezka = BFS(C, F, s, t)
            akt = 0
            for k in range(n):
                akt += F[s][k]
            #if i == 4 and j == 5: print(wynik, i, j, s, t, '\n', F, '\n', C)
            if akt > wynik: 
                wynik = akt
                if wynik == m_flow: return wynik
                #print(wynik, i, j)

    
    
    return wynik


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maxflow, all_tests = True )