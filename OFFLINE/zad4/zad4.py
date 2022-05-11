from zad4testy import runtests

def q_sort(A, p, r, pocz_ind):
    while p < r:
        q = partition(A, p, r, pocz_ind)
        if q - p < r - q:
            q_sort(A, p, q - 1, pocz_ind)
            p = q + 1
        else:
            q_sort(A, q + 1, r, pocz_ind)
            r = q - 1

def partition(A, p, r, pocz_ind):
    pivot = A[r]
    i = p - 1
    for j in range(p, r):
        if (A[j][2] < pivot[2]): # or (A[j][2] == pivot[2] and A[j][2] > pivot[2]):
            i += 1
            tmp = A[i]
            A[i] = A[j]
            A[j] = tmp
            tmp = pocz_ind[i]
            pocz_ind[i] = pocz_ind[j]
            pocz_ind[j] = tmp
    i += 1
    tmp = A[i]
    A[i] = A[r]
    A[r] = tmp
    tmp = pocz_ind[i]
    pocz_ind[i] = pocz_ind[r]
    pocz_ind[r] = tmp
    return i 

def bisearch(T, r):
    # k = r - 1
    # while k >= 0 and T[k][2] >= T[r][1]: k -= 1
    # return k
    x = T[r][1]
    l = 0
    mid = (l + r) // 2
    while l <= r: #(mid >= 0) and (mid + 1 <= r) and not (T[mid][2] < x and T[mid + 1][2] >= x):
        if T[mid][2] >= x: 
            r = mid - 1
        elif T[mid + 1][2] < x:
            l = mid + 1
        else: return mid
        #else: l = mid + 1
        mid = (l + r) // 2
    return -1
    # if mid == r or mid < 0: return -1
    # return mid


def select_buildings(T, p):
    n = len(T)
    poczatkowe_indeksy = [i for i in range(n)]

    # print("\nTablica T przed sortowaniem: ")
    # for i in range(n):
    #     print(T[i])
    
    q_sort(T, 0, n - 1, poczatkowe_indeksy)

    poprzedniki = [-1 for i in range(n)]
    for i in range(1, n):
        poprzedniki[i] = bisearch(T, i)

    # print("\nTablica poprzednikow: ")
    # for i in range(n):
    #     print(poprzedniki[i])

    # print("\nTablica T posortowana: ")
    # for i in range(n):
    #     print(T[i])
    
    # print("\nIndeksy: ")
    # for i in range(n):
    #     print(poczatkowe_indeksy[i])

    F = [[0 for b in range(p + 1)] for i in range(n)]

    # print("\nTablica F:")
    # for i in range(n):
    #     print(F[i])

    studenci = T[0][0] * (T[0][2] - T[0][1])
    for b in range(T[0][3], p + 1):
        F[0][b] = studenci

    for b in range(p + 1):
        for i in range(1, n):
            F[i][b] = F[i - 1][b]
            if T[i][3] <= b:
                k = poprzedniki[i]
                #while k >= 0 and T[k][2] >= T[i][1]: k -= 1
                if k >= 0:
                    # if b == p: print("\nk:", i, k, b - T[i][3])
                    studenci = T[i][0] * (T[i][2] - T[i][1])
                    F[i][b] = max(F[i][b], F[k][b - T[i][3]] + studenci)
                else: 
                    studenci = T[i][0] * (T[i][2] - T[i][1])
                    F[i][b] = max(F[i][b], studenci)

    # print("\nTablica F:")
    # for i in range(n):
    #     print(F[i])
    
    
    #print("\nPojemnosc: ", F[n - 1][p])
    wynik = []
    
    b = p 
    i = n - 1
    while i > 0:
        if F[i][b] == F[i - 1][b]:
            i -= 1
        else:
            wynik.append(poczatkowe_indeksy[i])
            studenci = T[i][0] * (T[i][2] - T[i][1])
            x = F[i][b] - studenci
            b -= T[i][3]
            i -= 1
            while i >= 0 and F[i][b] != x: i -= 1
            #i = poprzedniki[i]
    if i == 0 and F[0][b] > 0:
        wynik.append(poczatkowe_indeksy[0])



    #for i in range(n - 1, 0, -1):
    # # while i > 0:
    # #     if F[i][b] > F[i - 1][b]:
    # #         wynik.append(poczatkowe_indeksy[i])
    # #         studenci = T[i][0] * (T[i][2] - T[i][1])
    # #         if F[i][b] == studenci: 
    # #             # print("Wynik: ", wynik)            
    # #             return wynik
    # #         k = i - 1
    # #         while k >= 0 and T[k][2] >= T[i][1]: k -= 1
    # #         i = k + 1
    # #         b -= T[i][3]
    # #         #i wzięty
    # #     i -= 1
    
    # # if F[0][b] > 0:
    # #     wynik.append(poczatkowe_indeksy[0])
    
    # print("Wynik: ", wynik)

    return wynik
    
runtests( select_buildings )