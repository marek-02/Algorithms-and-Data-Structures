#Marek Żuwała
#dla k=1 zmodyfikowany buble sort, bez cofania
#dla k > 1 merge sort dla kolejnych co k kawałków o długości (max) 2k nodów, gwarantuje on że pierwsze k z tych 2k nodów będą już na swoich posortowanych miejscach
#złożoność: n/k * 2k * log2k, czyli
#O(n*logk)
from zad1testy import Node, runtests

#####################################################################
def split(s):
    l1 = l2 = None
    naZmiane = True
    p = s
    while p is not None:
        tmp = p.next
        if naZmiane:
            p.next = l1
            l1 = p
        else:
            p.next = l2
            l2 = p
        p = tmp
        naZmiane = not naZmiane


    return l1,l2
            

def merge(l1, l2):
    if l1.val < l2.val:
        tmp = l1.next
        l1.next = None
        lpoczatek = l1
        l1 = tmp
    else:
        tmp = l2.next
        l2.next = None
        lpoczatek = l2
        l2 = tmp
    
    lkoniec = lpoczatek
    
    while l1 is not None and l2 is not None:
        if l1.val < l2.val:
            tmp = l1.next
            l1.next = None
            lkoniec.next = l1
            l1 = tmp
        else:
            tmp = l2.next
            l2.next = None
            lkoniec.next = l2
            l2 = tmp
        lkoniec = lkoniec.next


    if l1 is None:
        lkoniec.next = l2
    else:
        lkoniec.next = l1
        
    while lkoniec.next is not None:
        lkoniec = lkoniec.next
    
    return lpoczatek, lkoniec
    

def mergeSort(start, k = 0):

    l1 = l2 = srodek = end = start
    
    if start is not None and start.next is not None:
        l1, l2 = split(start)
    
        l1, srodek, end = mergeSort(l1)
    
    
        l2, srodek, end = mergeSort(l2)
    
        start, end = merge(l1, l2)
    
    if k != 0:
        licznik = 1
        srodek = start
        while licznik < k:
            srodek = srodek.next
            licznik += 1
    
    return start, srodek, end

##################################################################### dokończyć - dużo fajniejsze, bez dodatkowej pamięci i może szybsze (?)

# def podciagRosnacy(s):
#     n = s
#     while n.next is not None and n.val < n.next.val:
#         n = n.next
#     return s, n

# def merge(l1, l2):
#     if l1.val < l2.val:
#         tmp = l1.next
#         l1.next = None
#         lpoczatek = l1
#         l1 = tmp
#     else:
#         tmp = l2.next
#         l2.next = None
#         lpoczatek = l2
#         l2 = tmp
    
#     lkoniec = lpoczatek
    
#     while l1 is not None and l2 is not None:
#         if l1.val < l2.val:
#             tmp = l1.next
#             l1.next = None
#             lkoniec.next = l1
#             l1 = tmp
#         else:
#             tmp = l2.next
#             l2.next = None
#             lkoniec.next = l2
#             l2 = tmp
#         lkoniec = lkoniec.next


#     if l1 is None:
#         lkoniec.next = l2
#     else:
#         lkoniec.next = l1
        
#     while lkoniec.next is not None:
#         lkoniec = lkoniec.next
    
#     return lpoczatek, lkoniec


# def mergeSort(start, k):
#     while True:
#         n = e = start
#         licznik = 0
#         while n is not None: 
#             s1, k1 = podciagRosnacy(n)
#             licznik += 1
#             n = k1.next
#             k1.next = None
#             if licznik == 1:
#                 if n is None: 
#                     e = k1
#                     break
#                 else:                        
#                     s2, k2 = podciagRosnacy(n)
#                     n = k2.next
#                     k2.next = None
#                     start, e = merge(s1, s2)
#             elif n is not None:
#                 s2, k2 = podciagRosnacy(n)
#                 n = k2.next
#                 k2.next = None
#                 e.next, e = merge(s1, s2)
#             else:
#                 e.next = s1                

#         if licznik == 1: break
    
#     srodek = start
#     licznik = 1
#     newk = k * 2
#     while srodek is not None and licznik < newk:
#         srodek = srodek.next
#         licznik += 1
#     if srodek is None: srodek = e
#     return start, srodek, e

#####################################################################



def lolAleBubel(start):
    if start.next is not None and start.val > start.next.val:
        tmp = start.next
        start.next = start.next.next
        start.next.next = start
        start = tmp
    
    prev, n = start, start.next
    while n.next is not None:
        if n.val > n.next.val:
            tmp = n.next
            n.next = n.next.next
            tmp.next = n
            prev.next = tmp
        prev = n
        n = n.next
    
    return start
        

def SortH(p, k):
    if k == 0: return p
    if k == 1: return lolAleBubel(p)
    
    s = n = p 
    prevS = e = tmp = None 
    licznik = 1

    while n is not None:
        if licznik == 2 * k: 
            tmp = n.next
            n.next = None
            if prevS is None:
                p, prevS, e = mergeSort(s, k)
            else:
                prevS.next, prevS, e = mergeSort(s, k)

            e.next = tmp    

            n = s = prevS.next
            licznik = 1
        else:
            n = n.next
            licznik += 1    

    if tmp is not None:
        prevS.next, prevS, e = mergeSort(s, k)
       
    
    if e is None:    
        p, prevS, e = mergeSort(s, k)
    
    return p

runtests( SortH ) 