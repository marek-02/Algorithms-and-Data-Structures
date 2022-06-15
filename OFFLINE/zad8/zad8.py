from zad8testy import runtests

def sqrt(x):
    return x**(0.5)

def ceil(x):
    return int(x) + int(x != int(x))

class Node: 
    def __init__(self, val):
        self.parent = self
        self.value = val

def find(x):
    if x.parent != x: 
        x.parent = find(x.parent)
    return x.parent

def union(x, y):
    x = find(x)
    y = find(y)
    if x == y: return 
    y.parent = x
        
def czySpojny(V):
    v = len(V)
    for i in range(v - 1):
        if find(V[i]) != find(V[i + 1]): return False
    return True

def highway(A):
    n = len(A)
    m = n * (n - 1) // 2 - 1
    V = [Node(i) for i in range(n)]
    G = [] 
    for j in range(n - 1):
        for i in range(j + 1, n):
            G.append([ceil(sqrt((A[i][0] - A[j][0])**2 + (A[i][1] - A[j][1])**2)), j, i])
    G.sort()

    wynik = G[-1][0] - G[0][0]
    aktWynik = 0
    i = -1
    j = 0
    
    while i < m:
        i += 1
        union(V[G[i][1]], V[G[i][2]])
        if czySpojny(V):
            for x in range(n):
                V[x].parent = V[x]
            j = i
            
            while not czySpojny(V):
                union(V[G[j][1]], V[G[j][2]])
                j -= 1
            j += 1
            aktWynik = G[i][0] - G[j][0]
            if aktWynik < wynik: wynik = aktWynik
            for x in range(n):
                V[x].parent = V[x]
            i = j

    if czySpojny(V):
            for x in range(n):
                V[x] = x
            j = i
            while not czySpojny(V):
                union(V, G[j][1], G[j][2])
                j -= 1
            j += 1
            aktWynik = G[i][0] - G[j][0]
            if aktWynik < wynik: wynik = aktWynik

    return wynik

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( highway, all_tests = True )