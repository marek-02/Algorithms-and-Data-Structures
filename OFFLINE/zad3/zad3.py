from zad3testy import runtests

class Node():
    def __init__(self, v):
        self.next = None
        self.v = v


class Kubelek():
    def __init__(self):
        self.first = None

    def dodaj(self, w):
        x = Node(w)
        if self.first is None:
            self.first = x
            return
        if w < self.first.v:
            x.next = self.first
            self.first = x
            return

        n_prev = self.first
        n = self.first
        while n is not None and n.v < w:
            n_prev = n
            n = n.next
        x.next = n
        n_prev.next = x


def bucket_sort(A):
    n = len(A)
    min = max = A[0]
    for i in range(n):
        if A[i] < min: min = A[i]
        elif A[i] > max: max = A[i]

    przedzial = (max - min) / n

    T = [Kubelek() for i in range(n + 1)]

    for i in range(n):
        x = int(((A[i] - min) / przedzial))
        T[x].dodaj(A[i])
    
    j = 0
    for i in range(n):
        while T[j].first is None: j += 1
        x = T[j].first.v
        T[j].first = T[j].first.next
        A[i] = x
    return A


def q_sort(A, p, r):
    while p < r:
        q = partition(A, p, r)
        if q - p < r - q:
            q_sort(A, p, q - 1)
            p = q + 1
        else:
            q_sort(A, q + 1, r)
            r = q - 1

def partition(A, p, r):
    pivot = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j][0] <= pivot[0]:
            i += 1
            tmp = A[i]
            A[i] = A[j]
            A[j] = tmp
    i += 1
    tmp = A[i]
    A[i] = A[r]
    A[r] = tmp
    return i 

def bin_search(A, l, p, x):
    # i = 0
    # while not (A[i][0] <= x and A[i][1] >= x): 
    #     i += 1
    # return i
    mid = (l + p) // 2
    while not (A[mid][0] <= x and A[mid][1] >= x): 
        if A[mid][0] > x: 
            p = mid - 1
            mid = (l + p) // 2
        else: #if A[mid][1] < x
            l = mid + 1
            mid = (l + p) // 2
        
    return mid


def SortTab(T, P):
    n = len(T)
    k = len(P)

    # for i in range(k):
    #     if P[i][2] == 0:
    #         tmp = P[i] #niepotrzebne
    #         P[i] = P[g - 1]
    #         P[g - 1] = tmp #niepotrzebne
    #         g -= 1


    q_sort(P, 0, k - 1)

    # print("Przed zmianami: ")
    # for i in range(k):
    #     print(P[i], end=" ")

    # print()
    
    last = P[0][1]
    P2 = [ [P[0][0], P[0][1]] ]
    for i in range(1, k):
        if last < P[i][1]: 
            x = max(last, P[i][0])
            P2.append([x, P[i][1]])
            last = P[i][1]
    k = len(P2)

    # print("Po zmianach: ")
    # for i in range(k):
    #     print(P2[i], end=" ")
            
    # return T    

    
    print("1")
    k_wst = [[] for i in range(k)]

    
    print("2")
    for i in range(n):
        indeks = bin_search(P2, 0, k - 1, T[i])
        k_wst[indeks].append(T[i])
        #k_wst[i % k].append(T[i])

    print("3")
    for i in range(k):
        if len(k_wst[i]) > 1: bucket_sort(k_wst[i])

    print("\nK: ", k, "\n")
    #print("4")
    j = 0
    k = 0
    for i in range(n):
        while len(k_wst[j]) - k == 0: 
            j += 1
            k = 0
        
        x = k_wst[j][k]
        k += 1
        T[i] = x


    return T

runtests( SortTab )