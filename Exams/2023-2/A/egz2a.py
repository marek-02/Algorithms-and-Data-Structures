from egz2atesty import runtests

def dominance(P):
    n = len(P)
    tx = [0] * (n+1)
    ty = [0] * (n+1)

    for x, y in P:
        tx[x] += 1
        ty[y] += 1

    Tx = [0] * (n+1)
    Ty = [0] * (n+1)

    Tx[n] = tx[n]
    Ty[n] = ty[n]

    for i in range(n - 1, -1, -1):
        Tx[i] = Tx[i + 1] + tx[i]
        Ty[i] = Ty[i + 1] + ty[i]

    return max(n - (Tx[i] + Ty[j]) + 1 for (i, j) in P)
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( dominance, all_tests = True )
