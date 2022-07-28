inf = float('inf')
from copy import copy

def comp(n, my_list = []):
    set_list = []
    for l in my_list:
        ll = copy(set(l))
        if 0 in ll:
            ll.remove(0)
        if n-1 in ll:
            ll.remove(n-1)
        set_list.append(copy(set(ll)))

    m = max(set_list, key=len)
    m = len(m)
    pruned = []
    for l in set_list:
        if len(l) == m and l not in pruned:
            pruned.append(l)

    while len(pruned) > 1:
        for i in range(m):
            n = min(pruned, key=lambda x: list(x)[i])
            n = list(n)[i]
            for l in pruned:
                if list(l)[i] > n:
                    pruned.remove(l)
    return list(pruned[0])

def bellman_ford(graph, time):
    n = len(graph)

    dist = [[inf for i in range(n)] for j in range(n)]
    dist[0][0] = 0

    for s in range(n):
        dist[s][s] = 0

        for _ in range(n - 1):
            for u in range(n):
                for v in range(n):
                    w = graph[u][v]
                    if dist[s][u] + w < dist[s][v]:
                        dist[s][v] = dist[s][u] + w

    for s in range(n):
        for u in range(n):
            for v in range(n):
                w = graph[u][v]
                if dist[s][u] + w < dist[s][v]:
                    return True, dist
        
    return False, dist

def dfs(graph, dist, visited = [0], time = 0, current = [0], temp_max = []):    
    n = len(graph)
    global_min = 0
    for i in range(n):
        for j in range(n):
            global_min = min(graph[i][j], global_min)

    if 0 not in visited:
        visited.append(0)

    prev = current[-1]

    if prev == n - 1 and time >= 0:
        temp_max = current

    has_neighbor = True
    for i in range(n):
        if graph[prev][i] != 0:
            has_neighbor = True

    temp = [copy(temp_max)]
    if has_neighbor:
        for u in range(n):
            if u != prev and time - dist[prev][u] >= global_min and (u not in visited or u == n-1):  
            # if u != prev and graph[prev][u] != 0 and time - dist[prev][u] >= global_min and (u not in visited or u == n-1):  
                current.append(u)
                visited.append(u)
                # print("visited = {}".format(visited))
                # print("{} -> {}".format(prev, u))
                temp.append(copy(dfs(graph, dist, visited, time - dist[prev][u], current)))
                current.pop()
                visited.pop()
    # print(temp)
    return comp(n, temp)

def solution(graph, time):
    max = []
    n = len(graph)
    has_cycle, dist = bellman_ford(graph, time)
    # print(dist)

    visited = []

    if not has_cycle:
        sol = dfs(graph, dist, visited, time)
        if 0 in sol:
            sol.remove(0)
        if n-1 in sol:
            sol.remove(n-1)
        return [x-1 for x in sol]
    return [x for x in range(0, n - 2)]





    
if __name__ == "__main__":
    print("Running ---------------------------")
    G1 = [[0, 1, 1, 1, 1], 
        [1, 0, 1, 1, 1], 
        [1, 1, 0, 1, 1], 
        [1, 1, 1, 0, 1], 
        [1, 1, 1, 1, 0]]
    print("Expecting: [0, 1], found {}".format(solution(G1, 3)))

    G2 = [[0, 2, 2, 2, -1], 
        [9, 0, 2, 2, -1], 
        [9, 3, 0, 2, -1], 
        [9, 3, 2, 0, -1], 
        [9, 3, 2, 2, 0]]
    print("Expecting: [1, 2], found {}".format(solution(G2, 1)))

    G3 = [[2, 2, 2, 2], 
        [2, 2, 2, 2], 
        [2, 2, 2, 2], 
        [2, 2, 2, 2]]
    print("Expecting: [], found {}".format(solution(G3, 1)))

    G4 = [[0, 5, 11, 11, 1],
        [10, 0, 1, 5, 1],
        [10, 1, 0, 4, 0],
        [10, 1, 5, 0, 1],
        [10, 10, 10, 10, 0]]
    print("Expecting: [0, 1], found {}".format(solution(G4, 10)))
    # # 0 -> 1 -> 2 -> 4

    G5 = [[0, 10, 10, 10, 1],
        [0, 0, 10, 10, 10],
        [0, 10, 0, 10, 10],
        [0, 10, 10, 0, 10],
        [1, 1, 1, 1, 0]]

    print("Expecting: [0, 1], found {}".format(solution(G5, 5)))

    G6 = [[0, 10, 10, 1, 10],
        [10, 0, 10, 10, 1],
        [10, 1, 0, 10, 10],
        [10, 10, 1, 0, 10],
        [1, 10, 10, 10, 0]]

    print("Expecting: [0, 1, 2], found {}".format(solution(G6, 6)))

    G7 = [[0, 2, 2, 2, -1],
        [9, 0, 2, 2, 0],
        [9, 3, 0, 2, 0],
        [9, 3, 2, 0, 0],
        [-1, 3, 2, 2, 0]]
    print("Expecting: [0, 1, 2], found {}".format(solution(G7, -500)))
    # print(bellman_ford(G7, -500))


