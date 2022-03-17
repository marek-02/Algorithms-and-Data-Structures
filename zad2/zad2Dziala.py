from zad2testy import runtests

def qSort(L, lewy, prawy):
    srodek = (lewy + prawy) // 2
    piwot = L[srodek]
    piwot = L[srodek]
    L[srodek] = L[prawy]

    j = lewy
    for i in range(lewy, prawy):
        if L[i][0] < piwot[0] or (L[i][0] == piwot[0] and L[i][1] > piwot[1]):
            L[i], L[j] = L[j], L[i]
            j += 1
    L[prawy] = L[j]
    L[j] = piwot

    if lewy < j - 1: qSort(L, lewy, j - 1)
    if prawy > j + 1: qSort(L, j + 1, prawy)




def depth(L):
    l = len(L)
    qSort(L, 0, l - 1)
    T = [0 for i in range(l)]
    G = [[0, 0] for i in range(l)]
    maxGora = L[0][1]
    G[0] = [maxGora, 0]
    g = 1

    for i in range(1, l):
        if L[i][1] > maxGora:
            maxGora = L[i][1]
            G[g] = [maxGora, i]
            g += 1
        else:
            j = g - 1
            while j >= 0 and L[i][1] <= G[j][0]:
                T[G[j][1]] += 1
                j -= 1
        
    result = 0
    for i in range(l):
        if T[i] > result: result = T[i]


    return result






runtests( depth ) 
