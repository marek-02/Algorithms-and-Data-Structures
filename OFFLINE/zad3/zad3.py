from zad3testy import runtests

def qSort(A, p, r):
    while p < r: #~2.73 (zoptymalizowana pamięć)
        q = partition(A, p, r)
        if q - p < r - q:
            qSort(A, p, q - 1)
            p = q + 1
        else:
            qSort(A, q + 1, r)
            r = q - 1

def partition(A, p, r):
    pivot = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j][0] < pivot[0] or (A[j][0] == pivot[0] and A[j][1] > pivot[1]):
            i += 1
            tmp = A[i]
            A[i] = A[j]
            A[j] = tmp
            #A[i], A[j] = A[j], A[i]
    i += 1
    tmp = A[i]
    A[i] = A[r]
    A[r] = tmp
    return i 
    #A[i + 1], A[r] = A[r], A[i + 1]


def SortTab(T,P):
    n = len(T)
    k = len(P)
    
    qSort(P, 0, k - 1)
    

    return sorted(T)

runtests( SortTab )