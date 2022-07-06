from zad1testy import runtests
from math import inf

def merge(T, p, q, r):
    L = T[p:q + 1]
    R = T[q + 1: r+ 1]

    L.append((inf, inf))
    R.append((inf, inf))

    i = j = 0
    for k in range(p, r + 1):
        if L[i][0] <= R[j][0]:
            T[k] = L[i]
            i += 1
        else:
            T[k] = R[j]
            j += 1

def merge_sort(T, p, r):
    if len(T) <= 1: return T
    
    if p < r: 
        m = (p + r) // 2
        merge_sort(T, p, m)
        merge_sort(T, m + 1, r)
        merge(T, p, m, r)

def chaos_index( T ):
    n = len(T)
    for i in range(n):
        T[i] = (T[i], i)
    
    merge_sort(T, 0, n - 1)
    max_chaotic = 0

    for i in range(n):
        if abs(i - T[i][1]) > max_chaotic: max_chaotic = abs(i - T[i][1])
    
    return max_chaotic


runtests( chaos_index )
