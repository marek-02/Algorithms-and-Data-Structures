from queue import PriorityQueue
from zad5testy import runtests

def plan(T):
    pq = PriorityQueue()
    wynik = [0]
    bak = T[0]
    for i in range(1, len(T) - 1):
        bak -= 1
        pq.put((-T[i], i))
        if bak == 0:
            tmp = pq.get()
            bak += -tmp[0]
            wynik.append(tmp[1])
    return sorted(wynik)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(plan, all_tests = True)