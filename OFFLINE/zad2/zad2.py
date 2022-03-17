from zad2testy import runtests

# def qSort(L, lewy, prawy):
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


def qSort(A, p, r):
    # if p < r:
    #     q = partition(A, p, r)
    #     qSort(A, p, q - 1)
    #     qSort(A, q + 1, r)
    while p < r:    
        q = partition(A, p, r)
        qSort(A, p, q - 1)
        p = q + 1
        
def partition(A, p, r):
    pivot = A[r]
    
    i = p - 1
    for j in range(p, r):
        if A[j][0] < pivot[0] or (A[j][0] == pivot[0] and A[j][1] > pivot[1]):
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


def depth(L):
    l = len(L)
    qSort(L, 0, l - 1)
    # return 0
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
                if G[j][1] < G[j + 1][1]:
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