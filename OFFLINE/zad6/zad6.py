#Marek Żuwała  
#Odpalam BFS'a z s, żeby zapamiętać odległości innych wierzchołków od s
#Potem funkcją znajdź przechodzę od t do s zapisując wszystkie ścieżki mające długość taką samą jak ta nakrótsza w tablicy Alternatywy
#jeśli w którymś momencie jest tylko jedna krawędź, która pozwala przejść w najszybszy sposób z s do t, to to jest nasza szukana krawędź

from collections import deque
from zad6testy import runtests

def wsadz(x, T):
    if x not in T: T.append(x)

def znajdz(t, Distance, G):
    d = Distance[t]
    Alternatywy = [[] for i in range(d + 1)]
    Alternatywy[d].append(t)
    Q = deque()
    Q.append(t)
    while Q:
        u = Q.popleft()
        du = Distance[u]
        for v in G[u]:
            dv = Distance[v]
            if dv == du - 1:
                wsadz(v, Alternatywy[dv])
                Q.append(v)

    for i in range(d):
        if len(Alternatywy[i]) == len(Alternatywy[i + 1]) and len(Alternatywy[i]) == 1: return (Alternatywy[i][0], Alternatywy[i + 1][0])
    
    return None

def BFS(G, s, t):
    n = len(G)
    Q = deque()
    Visited = [False for i in range(n)]
    Distance = [-1 for i in range(n)]

    Distance[s] = 0
    Visited[s] = True
    Q.append(s)
    
    while Q:
        u = Q.popleft()
        for v in G[u]:
            if not Visited[v]:
                Visited[v] = True
                Distance[v] = Distance[u] + 1
                Q.append(v)
    if Distance[t] == -1: return None

    return znajdz(t, Distance, G)
        
def longer(G, s, t):
    return BFS(G, s, t)

runtests( longer, all_tests = True)