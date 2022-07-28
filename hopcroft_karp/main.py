from collections import deque
import math

def red( x, y):
    # print("Reducing ", x, y)
    if x < y:
        x, y = 2 * x, y - x
    else:
        x, y = x - y, 2 * y
    return x, y
   
def is_solvable(x, y, dict = {}, prev = []):
    # x, y positive integers
    if (x, y) in dict:
        return dict[(x, y)]
    if (x,y) in prev:
        dict[(x, y)] = True
        return True
    if x == y:
        dict[(x,y)] = False
        return False
    else:
        prev.append((x, y))
        x, y = red(x, y)
        return is_solvable(x, y, dict, prev)    
       
def construct_graph(l):
    # Constructs an adjacency matrix from the banana list
    k = len(l)
    # make empty graph
    M = [[0 for i in range(k)] for j in range(k)]
    # for row in M:
        # print(row)
   
    # Iterate through all possible pairs and put a 1 in the i, j and j, i entries
    for i in range(k):
        for j in range(i + 1, k):
            if is_solvable(l[i], l[j]):
                M[i][j] = 1
    return M


class HopkroftCarp:
    def __init__(self, adj = []):
        # construct our graph as a dictionary
        self.G = {}
        for i in range(len(adj)):
            self.G[i] = []
            for j in range(i + 1, len(adj)):
                if adj[i][j] == 1:
                    self.G[i].append(j)


        self.U = []
        self.V = []
        k = len(adj)

        for i in range(k):
            self.U.append(i)
            self.V.append(i)


        self.pairU = {}
        self.pairV = {}
        self.dist = {}
        self.NIL = -1
        self.Q = deque()
    
    def BFS(self):
        # Q = deque()
        for u in self.U:
            if self.pairU[u] == self.NIL:
                self.dist[u] = 0
                self.Q.append(u)
            else:
                self.dist[u] = 'inf'

        # Goal is to reach NIL vertex. 
        #  When that happens, the distance to NIL is set as < inf
        self.dist[self.NIL] = 'inf'

        while len(self.Q) > 0:
            curr = self.Q.popleft()
            if self.dist[curr] < self.dist[self.NIL]:
            # if curr != self.NIL:
                for neighbor in self.G[curr]:
                    if self.dist[self.pairV[neighbor]] == 'inf':
                        self.dist[self.pairV[neighbor]] = self.dist[curr] + 1
                        self.Q.append(self.pairV[neighbor])
        return self.dist[self.NIL] != 'inf'

    def DFS(self, start):
        if start != self.NIL:
            for neighbor in self.G[start]:
                if self.dist[self.pairV[neighbor]] == self.dist[start] + 1:
                    if self.DFS(self.pairV[neighbor]):
                        self.pairV[neighbor] = start
                        self.pairU[start] = neighbor
                        return True
            self.dist[start] = 'inf'
            return False
        return True

    def hopcroft_karp(self):
        for  u in self.U:
            self.pairU[u] = self.NIL
        for v in self.V:
            self.pairV[v] = self.NIL
        
        matching = 0

        while self.BFS():
            print(self.pairU)
            for u in self.U:
                if self.pairU[u] == self.NIL:
                    if self.DFS(u):
                        print("Increasing matching for {}".format(str(u) + ", " +  str(self.pairU[u])))
                        matching += 1
        return matching
                    
                





if __name__ == "__main__":
    banana_list = [1, 7, 3, 21, 13, 19]
    adj = construct_graph(banana_list)

    HK1 = HopkroftCarp(adj)
    matching = HK1.hopcroft_karp()
    print("Matching number = {}".format(matching))
    print("G = {}".format(HK1.G))
    print("Pairing = {}".format(HK1.pairU))


    # l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # HK2 = HopkroftCarp(construct_graph(l))
    # HK2.hopcroft_karp()
    # print(HK2.G)


    