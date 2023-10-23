# całe rozwiązanie oparte na obserwacji, że jeśli obrabujemy jakiś zamek to dalej idziemy po opodatkowanych krawędziach
# czyli jeżeli chcemy obrabować jakiś zamek to dochodzimy do niego z początkowego zamku najkrótszą drogą oryginalnymi krawędziami, 
# a potem opodatkowanymi idziemy do zamku końcowego

from egz1Atesty import runtests

from queue import PriorityQueue
from math import inf

# standartowy dijkstra 
# O(ElogV)
def dijkstra_start(graph, source): 
  queue = PriorityQueue()
  distance = [inf] * len(graph)
  n = len(graph)
  queue.put((0, source))
  while not queue.empty() and n > 0:
    dist, v = queue.get()
    if dist < distance[v]:
      n -= 1
      distance[v] = dist
      for edge in graph[v]:
        u, length = edge
        queue.put((dist + length, u))
  return distance

# zmieniony dijkstra - zamiast oryginalnych wartości krawędzi liczy te opodatkowane (czyli * 2 + r)
# O(ElogV)
def dijkstra_end(graph, source, r): 
  queue = PriorityQueue()
  distance = [inf] * len(graph)
  n = len(graph)
  queue.put((0, source))
  while not queue.empty() and n > 0:
    dist, v = queue.get()
    if dist < distance[v]:
      n -= 1
      distance[v] = dist
      for edge in graph[v]:
        u, length = edge
        queue.put((dist + length * 2 + r, u))
  return distance

# całe rozwiązanie ma złożoność O(ElogV) = O(V^2 * logV)
def gold(G,V,s,t,r):
  n = len(G)

  #liczę najkrótsze odległości od zamku początkowego - O(ElogV)
  distances_from_start = dijkstra_start(G, s)

  #liczę najkrótsze odległości od zamku końcowego, idąc po opodatkowanych krawędziach - O(ElogV)
  distances_from_end = dijkstra_end(G, t, r) 

  #jako początek przejście bez rabowania żadnego zamku - O(1)
  result = distances_from_start[t] 

  #O(V)
  for i in range(n): 
    #ile będzie nas kosztować trasa jeśli obrabujemy zamek i - O(1)
    result_if_castle_i_taken = distances_from_start[i] + distances_from_end[i] - V[i] 

    if result_if_castle_i_taken < result: 
      result = result_if_castle_i_taken
  
  return result

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( gold, all_tests = True )