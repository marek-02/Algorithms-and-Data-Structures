from re import T
from zad3testy import runtests

def insert_sort(A):
    n = len(A)
    for i in range(1, n):
        x = A[i]
        j = i - 1
        while j >= 0 and A[j] > x:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = x
    return A

def bucket_sort(A):
    n = len(A)
    max_el = max(A)
    min_el = min(A)
    przedzial = (max_el - min_el) / (n // 2)

    T = [[] for i in range((n // 2) + 1)]

    for i in range(n):
        x = int((A[i] - min_el) / przedzial)
        T[x].append(A[i])
    
    for t in T:
        if len(t) != 0: insert_sort(t)

    k = 0
    for t in T:
        if t:
            for i in t:
                A[k] = i
                k += 1

    return A


def q_sort(A, p, r):
    while p < r:
        q = partition(A, p, r)
        if q - p < r - q:
            q_sort(A, p, q - 1)
            p = q + 1
        else:
            q_sort(A, q + 1, r)
            r = q - 1

def partition(A, p, r):
    pivot = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= pivot:
            i += 1
            tmp = A[i]
            A[i] = A[j]
            A[j] = tmp
    i += 1
    tmp = A[i]
    A[i] = A[r]
    A[r] = tmp
    return i 

def bin_search(A, l, p, x):
    mid = (l + p) // 2

    while not (A[mid] <= x and A[mid + 1] >= x): 
        if A[mid] > x: 
            p = mid - 1
            mid = (l + p) // 2
        else: #if A[mid][1] < x
            l = mid + 1
            mid = (l + p) // 2
        
    return mid


def SortTab(T, P):
    n = len(T)
    k = len(P)

    P2 = [P[i][0] for i in range(k)]
    for i in range(k): P2.append(P[i][1])
    k *= 2
    
    q_sort(P2, 0, k - 1)
    
    k_wst = [[] for i in range(k)]
    

    for i in range(n):
        indeks = bin_search(P2, 0, k - 1, T[i])
        k_wst[indeks].append(T[i])


    for kub in k_wst:
        if len(kub) > 1: bucket_sort(kub)

    k = 0
    for kub in k_wst:
        if kub:
            for i in kub:
                T[k] = i
                k += 1

    return T

runtests( SortTab )