from queue import Queue


class Edge:
    def __init__(self, v, flow, C, rev):
        self.v = v
        self.flow = flow
        self.C = C
        self.rev = rev

class Graph:
    def __init__(self, V):
        self.adj = [[] for i in range(V)]
        self.V = V
        self.level = [0 for i in range(V)]
    
    def addEdge(self, u, v, C):
        a = Edge(v, 0, C, len(self.adj[v]))
        b = Edge(u, 0, 0, len(self.adj[u]))

        self.adj[u].append(a)
        self.adj[v].append(b)

    def BFS(self, s, t):
        for i in range(self.V):
            self.level[i] = -1
        
        self.level[s] = 0

        Q = Queue()
        Q.put(s)
        while not Q.empty():
            u = Q.get()
            for i in range(len(self.adj[u])):
                e = self.adj[u][i]
                if self.level[e.v] < 0 and e.flow < e.C:
                    self.level[e.v] = self.level[u] + 1
                    Q.put(e.v)
        
        return False if self.level[t] < 0 else True
    
    def sendFlow(self, u, flow, t, start):
        if u == t:
            return flow
        
        while start[u] < len(self.adj[u]):
            e = self.adj[u][start[u]]

            if self.level[e.v] == self.level[u] + 1 and e.flow < e.C:
                curr_flow = min(flow, e.C - e.flow)
                temp_flow = self.sendFlow(e.v, curr_flow, t, start)

                if temp_flow and temp_flow > 0:
                    e.flow += temp_flow

                    self.adj[e.v][e.rev].flow -= temp_flow
                    return temp_flow
            start[u] += 1
    
    def DinicMaxflow(self, s, t):
        if s == t: return -1

        result = 0
        
        while self.BFS(s,t):
            start = [0 for i in range(self.V)] #?
            while True:
                flow = self.sendFlow(s, float('inf'), t, start)
                if not flow:
                    break

                result += flow
        return result

g = Graph(6)
g.addEdge(0, 1, 4)
g.addEdge(0, 3, 3)
g.addEdge(1, 3, 2)
g.addEdge(1, 2, 2)
g.addEdge(3, 2, 2)
g.addEdge(3, 4, 3)
g.addEdge(2, 5, 4)
g.addEdge(4, 5, 5)
print("Maximum flow", g.DinicMaxflow(0,5))