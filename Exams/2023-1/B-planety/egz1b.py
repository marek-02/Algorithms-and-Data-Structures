from egz1btesty import runtests

from math import inf

# całe rozwiązanie ma złożoność O(nE)
def planets( D, C, T, E ):
    n = len(D)
    # zainicjowanie tablicy, która odpowiada funkcji z podpowiedzi 
    # F[i][b] to minimalny koszt znalezienia się na planecie i, posiadając jeszcze b ton paliwa w baku - O(nE)
    F = [[inf for i in range(E + 1)] for i in range(n)] 
    
    # rozpatrzenie pierwszego rzędu osobno - żeby mieć i paliwa na pierwszej planecie trzeba ją tutaj kupić - O(E)
    for i in range(E + 1):
        F[0][i] = i * C[0]

    # rozpatrzenie teleportu z pierwszej planety
    dest, cost = T[0]
    if dest != 0:
        F[dest][0] = cost

    # pętla, która odpowiada za rekurencyjne zależności i dynamiczne programowanie - O(nE)
    for i in range(1, n):
        # odległość z poprzedniej planety
        dist = D[i] - D[i - 1] 

        # rozpatrzenie przybycia na tą planetę z pustym bakiem osobno 
        # można to zrobić jedynie mając 'dist' paliwa na poprzedniej planecie (chyba, że się tu dostało teleportem - dlatego minimum)
        F[i][0] = min(F[i][0], F[i - 1][dist]) 
        
        # znając już minimalny koszt dodarcia do tej planety i posiadania pustego baku można rozpatrzyć dalszy teleport
        dest, cost = T[i]
        if dest != i:
            F[dest][0] = min(F[dest][0] , F[i][0] + cost) 

        # uzupełnienie dalszych wartości - czyli bycia na planecie i, mając j paliwa w baku
        for j in range(1, E + 1):
            # można to zrobić kupując kolejną tone paliwa (dodajemy do minimalnej ceny bycia na tej planecie z jedną toną paliwa mniej - niekoniecznie kupujemy tutaj j ton paliwa)
            F[i][j] = F[i][j - 1] + C[i]
            #lub 'biorąc' paliwo, które zostało z poprzedniej planety, o ile to możliwe
            if j + dist <= E:
                F[i][j] = min(F[i][j], F[i - 1][j + dist])
    
    # wynik to oczywiście minimalny koszt dodarcia do ostatniej paliwy z pustym bakiem
    return F[n - 1][0]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( planets, all_tests = True )
