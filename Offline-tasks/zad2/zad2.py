#Marek Żuwała   
#Algorytm na początku przechodzi przez daną tablicę i dzieli elementy
#na te, które mogą zawierać najwięcej przedziałów (nie zawierają się w żadnym innym) - Kandydaci
#oraz te, które zawierają się w jakimś innym - Leszcze
#potem przechodzi leszczami po kandydatach i oblicza, który przedział zawiera najwięcej przedziałów 
#złożoność pesymistycznie O(n^2), ale średnia n logn (?), działa sporo szybciej niż algorytm z sortem, który wcześniej zaimplementowałem
from zad2testy import runtests

class Node():
    def __init__(self, d, g):
        self.d = d
        self.g = g
        self.w = 0
        self.next = None

def depth(L):
    l = len(L)
    Kandydaci = Node(-1, -1)
    Kandydaci.next = Node(L[0][0], L[0][1])

    Leszcze = []

    for i in range(1, l): #ustala kandydatów
        nPrev = Kandydaci
        n = Kandydaci.next
        czyMozeSieLiczyc = True
        while n is not None:
            if czyMozeSieLiczyc and L[i][0] < n.d and L[i][1] < n.g: #może być kandydatem, dodajemy
                tmp = Node(L[i][0], L[i][1])
                tmp.next = n
                nPrev.next = tmp
                czyMozeSieLiczyc = False
                break
            if L[i][0] >= n.d and L[i][1] <= n.g: #zawiera się w jakimś z kandydatów, olewamy
                Leszcze.append([L[i][0], L[i][1]])
                czyMozeSieLiczyc = False
                break
            elif L[i][0] <= n.d and L[i][1] >= n.g: #wyrzuca kandydatów których zawiera
                nPrev.next = n.next #wywala n
                Leszcze.append([n.d, n.g])
                n = nPrev.next
            else: #większy dół i większa góra - idziemy dalej żeby znaleźć miejsce gdzie go wsadzić
                nPrev = n
                n = n.next
        if czyMozeSieLiczyc: nPrev.next = Node(L[i][0], L[i][1])

    result = 0

    j = len(Leszcze)
    for i in range(j):
        kandydat = Kandydaci.next
        while kandydat is not None and Leszcze[i][0] >= kandydat.d:
            if Leszcze[i][1] <= kandydat.g: # and Leszcze[i][0] >= kandydat.d:
                kandydat.w += 1
            kandydat = kandydat.next


    kandydat = Kandydaci.next
    while kandydat is not None:
        if kandydat.w > result:
            result = kandydat.w
        kandydat = kandydat.next          

    # print("Tablica: ")
    # for i in range(l):
    #     print("[", L[i][0], ", ", L[i][1], "]", end = ", ")
    # print()

    # print("Leszcze: ")
    # for i in range(j):
    #     print("[", Leszcze[i][0], ", ", Leszcze[i][1], "]", end = ", ")
    # print()

    # print("Leszcze w dobrym: ")
    # for i in range(j):
    #     if Leszcze[i][1] <= 93 and Leszcze[i][0] >= 6:
    #         print("[", Leszcze[i][0], ", ", Leszcze[i][1], "]", end = ", ")

    # print()
    # print("Leszcze niezałapane: ")
    # for i in range(j):
    #     if not (Leszcze[i][1] <= 93 and Leszcze[i][0] >= 6):
    #         print("[", Leszcze[i][0], ", ", Leszcze[i][1], "]", end = ", ")

    # print()
    # print("Kandydaci: ")
    # kandydat = Kandydaci.next
    # while kandydat is not None:
    #     print("[", kandydat.d, ", ", kandydat.g, "]", end = ", ")
    #     kandydat = kandydat.next
    #print(git.d, git.g)

    return result


runtests( depth ) 