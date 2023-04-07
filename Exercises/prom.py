def f(T, n, C, i, l1, l2):
    if i == n or l1 < 0 or l2 < 0: return 0
    if C[l1][l2] == -1:
        if l1 - T[i] >= 0 and l2 - T[i] >= 0:
            C[l1][l2] = max(f(T, n, C, i + 1, l1 - T[i], l2), f(T, n, C, i + 1, l1, l2 - T[i])) + 1
        elif l1 - T[i] >= 0:
            C[l1][l2] = f(T, n, C, i + 1, l1 - T[i], l2) + 1
        else:
            C[l1][l2] = f(T, n, C, i + 1, l1, l2 - T[i]) + 1
    return C[l1][l2]

def F(T, L):
    n = len(T)
    l1 = l2 = L
    C= [[-1 for j in range(L + 1)] for i in range(L + 1)]
    C[0][0] = 0

    a = f(T, n, C, 0, l1, l2)
    for x in C:
        print(x)
    return a

L = 20
T = [13, 5, 3, 4, 2, 6, 1, 8, 9, 1, 2, 14]

x = F(T, L)
print(x)