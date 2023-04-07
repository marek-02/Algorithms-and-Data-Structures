def bi_search(T, x):
    if x <= T[0][-1]: return 0
    
    l = 0
    r = len(T) - 1

    while l <= r:
        mid = (l + r) // 2
        if mid > 0 and x > T[mid - 1][-1] and x <= T[mid][-1]:
            return mid
        elif x > T[mid][-1]:
            l = mid + 1
        else: 
            r = mid - 1
    return l

def podciag(T):
    wynik = [
            [T[0]]
                ]
    wynik_rozmiar = 0

    for i in range(1, len(T)):
        indeks = bi_search(wynik, T[i])
        if indeks > wynik_rozmiar:
            wynik.append([])
            wynik_rozmiar += 1
        wynik[indeks].append(T[i])
    
    print(wynik)
    return len(wynik)

T = [7, 2, 9, 6, 10, 3, 4, 8, 7, 8, 5, 9, 11]
x = podciag(T)
print(x)