def bi_search(A, kloc):
    l = 0
    r = len(A) - 1
    mid = (l + r) // 2
    
    print("A: ", A)
    print()
    
    while l <= r:
        mid = (l + r) // 2
        if mid < len(A) - 1 and (A[mid][-1][0] <= kloc[0] and A[mid][-1][1] >= kloc[1]) and (A[mid + 1][-1][0] > kloc[0] or A[mid + 1][-1][1] < kloc[1]):
            return mid + 1
        elif (A[mid][-1][0] > kloc[0] or A[mid][-1][1] < kloc[1]):
            r = mid - 1
        else: 
            l = mid + 1
    if r == -1:
        return 0
    return l

def klocki(T):
    n = len(T)
    wynik = [[]]
    wn = -1
    for klocek in T:
        if wn == -1:
            wynik[0].append(klocek)
            wn += 1
        else:
            indeks = bi_search(wynik, klocek)
            if indeks > wn:
                wynik.append([])
                wn += 1
            wynik[indeks].append(klocek)
    print("A: ", wynik)
    return n - len(wynik)

T = [ [10, 90],
      [30, 40],
      [20, 80],
      [30, 110],
      [30, 75],
      [30, 80],
      [0, 130],
      [40, 60],
      [50, 55],
      [50, 52] ]

print(klocki(T))