from queue import PriorityQueue
import queue
from zad2testy import runtests


def robot( L, A, B ):
    w = len(L)
    k = len(L[0])
    Graph = [[[[-1 for _ in range(3)] for _ in range(4)] for _ in range(k)] for _ in range(w)]
    qp = PriorityQueue()
    qp.put((0, A[0], A[1], 0, 0))
    #time, x, y, direction, idx
    possible_moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    seconds = [60, 40, 30]
    while not qp.empty():
        time, x, y, direction, idx = qp.get()
        
        if(x, y) == B: return time

        if x >= k or y >= w or Graph[y][x][direction][idx] != -1 or L[y][x] == 'X':
            continue
        Graph[y][x][direction][idx] = time
        qp.put((time + 45, x, y, (direction + 1) % 4, 0))
        qp.put((time + 45, x, y, (direction + 3) % 4, 0))
        x += possible_moves[direction][0]
        y += possible_moves[direction][1]
        qp.put((time + seconds[idx], x, y, direction, min(idx + 1, 2)))
    
    return None

    
runtests( robot )

