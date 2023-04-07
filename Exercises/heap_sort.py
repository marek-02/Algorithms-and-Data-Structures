def left(i): return 2 * i + 1
def right(i): return 2 * i + 2
def parent(i): return (i - 1) // 2

################################################################################

def heapify_down(A, n, i): #naprawianie kopca (w dół) zepsutego w miejscu i, n to liczba elementów w kopcu
    l = left(i)
    r = right(i)
    max_ind = i
    if l < n and A[l] > A[max_ind]:
        max_ind = l
    if r < n and A[r] > A[max_ind]:
        max_ind = r
    if max_ind != i: 
        tmp = A[i]
        A[i] = A[max_ind]
        A[max_ind] = tmp
        heapify_down(A, n, max_ind)

def build_heap(A):
    n = len(A)
    for i in range(parent(n - 1), -1, -1):
        heapify_down(A, n, i)
        #print(A)

def heap_sort(A):
    n = len(A)
    build_heap(A)
    #build_heap_up(A)
    for i in range(n - 1, 0, -1):
        A[0], A[i] = A[i], A[0]
        heapify_down(A, i, 0)

################################################################################

def heapify_up(A, i):
    p = parent(i)
    if p >= 0 and A[p] < A[i]:
        A[p], A[i] = A[i], A[p]
        heapify_up(A, p)

def build_heap_up(A):
    n = len(A)
    for i in range(1, n):
        heapify_up(A, n, i)
        #print(A)


A = [1, 8, 2, 4, 3, 5, 7, 2, 13, 5]
heap_sort(A)
print("Posortowany: ", A)