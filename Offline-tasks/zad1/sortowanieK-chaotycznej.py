#Marek Żuwała
#zrobić opis (pierwsze zadanie offline)

from zad1testy import Node, runtests

# class Node:
#     def __init__(self, v):
#         self.val = v
#         self.next = None
#     def dodaj(self, v):
#         n = Node(v)
#         n.next = self.next
#         self.next = n
    
#     def dodajNoda(self, n):
#         n.next = self.next
#         self.next = n
    
#     def wypisz(self):
#         n = self
#         while n is not None:
#             print(n.val, end=" ")
#             n = n.next
#         print()

def kQuickSort(start, koniec, k, licznik):
    t = start.next
    prev = start
    pivot = start
    ileNaLewo = 0
    
    while t is not koniec:
        if t.val < pivot.val:
            prev.next = t.next
            t.next = start
            start = t
            t = prev.next
            ileNaLewo += 1
        else:
            prev = t       
            t = t.next
    
    if ileNaLewo > k + 1:
        start = kQuickSort(start, pivot, k, ileNaLewo)


    ileNaPrawo = licznik - ileNaLewo - 1
    if ileNaPrawo > k + 1:
        pivot.next = kQuickSort(pivot.next, t, k, ileNaPrawo)
    
    return start


def sortH(p, k):
    t = p.next
    prev = p
    pivot = p
    licznik = 1
    ileNaLewo = 0
    while t is not None:
        licznik += 1
        if t.val < pivot.val:
            prev.next = t.next
            t.next = p
            p = t
            t = prev.next
            ileNaLewo += 1
        else:
            prev = t       
            t = t.next
    if ileNaLewo > k + 1:
        p = kQuickSort(p, pivot, k, ileNaLewo)
    ileNaPrawo = licznik - ileNaLewo - 1
    if ileNaPrawo > k + 1:
        pivot.next = kQuickSort(pivot.next, t, k, ileNaPrawo)
    
    return p
    
runtests( sortH ) 

# A = Node(14)
# A.dodaj(8)
# A.dodaj(6)
# A.dodaj(3)
# A.dodaj(1)
# A.dodaj(7)
# A.dodaj(0)
# A.dodaj(2)
# A.wypisz()
# A = sortH(A, 0)
# A.wypisz()
