from zad2testy import runtests

# def qSort1(L, lewy, prawy): #~2.75
#     srodek = (lewy + prawy) // 2
#     piwot = L[srodek]
#     piwot = L[srodek]
#     L[srodek] = L[prawy]

#     j = lewy
#     for i in range(lewy, prawy):
#         if L[i][0] < piwot[0] or (L[i][0] == piwot[0] and L[i][1] > piwot[1]):
#             L[i], L[j] = L[j], L[i]
#             j += 1
#     L[prawy] = L[j]
#     L[j] = piwot

#     if lewy < j - 1: qSort(L, lewy, j - 1)
#     if prawy > j + 1: qSort(L, j + 1, prawy)

# def qSor(A): #~2.78
#     l = len(A)
#     S = [(-1, -1) for i in range(l)]
#     S[0] = (0, l - 1)
#     ptr = 0

#     while ptr >= 0:
#         p, r = S[ptr]
#         ptr -= 1
#         q = partition(A, p, r)

#         if q - 1 > p:
#             ptr += 1
#             S[ptr] = (p, q - 1)
        
#         if q + 1 < r:
#             ptr += 1
#             S[ptr] = (q + 1, r)


def qSort(A, p, r):
    # if p < r: #~2.72
    #     q = partition(A, p, r)
    #     qSort(A, p, q - 1)
    #     qSort(A, q + 1, r)
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


def depth(L):
    l = len(L)
    #qSor(L)
    qSort(L, 0, l - 1)
    #qSort1(L, 0, l - 1)
    #return 0
    G = []
    maxGora = L[0][1]
    G.append([maxGora, 0])
    g = 1
    S = 0

    for i in range(1, l):
        if L[i][1] > maxGora:
            maxGora = L[i][1]
            G.append([maxGora, 0])
            g += 1
        else:
            G[g - 1][1] += 1
            j = g - 2
            while j >= S:
                if G[S][1] <= G[j + 1][1]:
                    S = j + 1
                    break
                if L[i][1] > G[j][0]:
                    break
                G[j][1] += 1
                j -= 1   

    result = G[S][1]
    #S += 1
    # while S < g:
    #     if G[S][1] > result: result = G[S][1]
    #     S += 1


    return result


runtests( depth ) 