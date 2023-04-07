def counting_sort(A, k): #O(n + k), k - liczby z przedziału <0, k - 1>
    n = len(A)
    C = [0 for i in range(k)]
    B = [0 for i in range(n)]
    
    for x in A: C[x] += 1
    
    for i in range(1, k): C[i] += C[i - 1]

    for i in range(n - 1, -1, -1):
        B[C[A[i]] - 1] = A[i]
        C[A[i]] -= 1
    
    for i in range(n): A[i] = B[i]

def counting_sort_for_classic_radix_sort(A, d):
    n = len(A)
    B = [0 for i in range(n)]
    C = [0 for i in range(10)] #system dziesiątkowy i sortowanie po kolei od cyfry najmniej znaczącej
    for i in range(n):
        index = A[i] // d
        C[index % 10] += 1
    #print(A, C)
    
    for i in range(1, 10): C[i] += C[i - 1]
    #print(C)
    for i in range(n - 1, -1, -1):
        index = A[i] // d
        #print(A[i], C[index % 10] - 1)
        B[C[index % 10] - 1] = A[i]
        C[index % 10] -= 1
    
    for i in range(n): A[i] = B[i]


def radix_sort(A): #klasyczne - system dziesiątkowy i sortowanie po kolei od cyfry najmniej znaczącej
    max_in_A = max(A)
    #print(A, max_in_A)
    d = 1
    while max_in_A / d > 1:
        counting_sort_for_classic_radix_sort(A, d)
        d *= 10


# A = [4312, 2135, 1012, 253, 101, 197, 99, 8512, 11111, 2010]
# radix_sort(A)
# print(A)

A = [ [1, 2, 3], [0, 4], [], [7, 8, 0]]

B = [j for i in A for j in i]

print(B)

# a = ord(c)
# b = chr(a)
# print(a, b)