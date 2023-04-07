#struktura, która w logn dodaje elementy do zbioru i zwraca mediane zbioru, maksymalnie około 2 * n elementów w zbiorze

class Node():
    def __init__(self, n, v):
        self.mediana = v
        self.heap_max = [0 for i in range(n)]
        self.n = 0
        self.heap_min = [0 for i in range(n)]
        self.m = 0

def heapify_up_max(T, i):
    p = (i - 1) // 2
    if p >= 0 and T[p] < T[i]:
        T[p], T[i] = T[i], T[p]
        heapify_up_max(T, p)

def heapify_down_max(A, n, i): 
    l = 2 * i + 1
    r = 2 * i + 2
    max_ind = i
    if l < n and A[l] > A[max_ind]:
        max_ind = l
    if r < n and A[r] > A[max_ind]:
        max_ind = r
    if max_ind != i: 
        tmp = A[i]
        A[i] = A[max_ind]
        A[max_ind] = tmp
        heapify_down_max(A, n, max_ind)


def add_to_heap_max(T, n, val):
    T[n] = val
    heapify_up_max(T, n)

def pop_from_heap_max(T, n):
    T[0], T[n - 1] = T[n - 1], T[0]
    heapify_down_max(T, n - 1, 0)
    return T[n - 1]




def heapify_up_min(T, i):
    p = (i - 1) // 2
    if p >= 0 and T[p] > T[i]:
        T[p], T[i] = T[i], T[p]
        heapify_up_min(T, p)

def heapify_down_min(A, m, i): 
    l = 2 * i + 1
    r = 2 * i + 2
    max_ind = i
    if l < m and A[l] < A[max_ind]:
        max_ind = l
    if r < m and A[r] < A[max_ind]:
        max_ind = r
    if max_ind != i: 
        tmp = A[i]
        A[i] = A[max_ind]
        A[max_ind] = tmp
        heapify_down_min(A, m, max_ind)


def add_to_heap_min(T, m, val):
    T[m] = val
    heapify_up_min(T, m)

def pop_from_heap_min(T, m):
    T[0], T[m - 1] = T[m - 1], T[0]
    heapify_down_min(T, m - 1, 0)
    return T[m - 1]


def dodaj(A, v):
    if v <= A.mediana:
        if A.n == A.m == 0:
            add_to_heap_max(A.heap_max, A.n, v)
            A.n += 1
        elif A.n > A.m:
            add_to_heap_min(A, A.m, A.mediana)
            A.m += 1    
            add_to_heap_max(A.heap_max, A.n, v)
            A.n += 1
            A.mediana = pop_from_heap_max(A.heap_max, A.n)
            A.n -= 1
        else:
            add_to_heap_max(A.heap_max, A.n, v)
            A.n += 1
    else:
        if A.n == A.m == 0:
            add_to_heap_max(A.heap_max, A.n, A.mediana)
            A.n += 1
            A.mediana = v
        elif A.n > A.m:
            add_to_heap_min(A.heap_min, A.m, v)
            A.m += 1
        else:
            add_to_heap_max(A.heap_max, A.n, A.mediana)
            A.n += 1    
            add_to_heap_min(A.heap_min, A.m, v)
            A.m += 1
            A.mediana = pop_from_heap_min(A.heap_min, A.m)
            A.m -= 1
    print("Po dodaniu: ", A.mediana, A.heap_max, A.n, A.heap_min, A.m)


def get_median(A):
    if A.n == A.m: 
        x = A.mediana
    else: 
        x = (A.mediana + pop_from_heap_max(A.heap_max, A.n)) / 2
        A.n -= 1
    A.mediana = pop_from_heap_min(A.heap_min, A.m)
    A.m -= 1
    return x

A = Node(5, 1)
dodaj(A, 2)
dodaj(A, 5)
dodaj(A, 4)
dodaj(A, 7)
dodaj(A, 10)
dodaj(A, 25)
med = get_median(A)
print(med, A.heap_max, A.n, A.heap_min, A.m)

dodaj(A, 123)
dodaj(A, 6)
med = get_median(A)
print(med, A.heap_max, A.n, A.heap_min, A.m)

# A = [[1, 2, 3], [0, 4, 10], [], [1, 1, 1, 1, 1]]
# x = [i for i in A for i in i]
# print(x)