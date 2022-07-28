from random import randint
from copy import copy

def dfs(G, current = 0, visited = []):
    n = len(G)
    # print(visited)

    if len(visited) == 0:
        visited.append(current)

    # termination condition
    # check for any neighbors
    has_neighbor = False
    for i in range(n):
        if G[current][i] != 0 and i != current and i not in visited:
            print("{} -> {}".format(current, i))
            has_neighbor = True

    # if there are no more unvisited neighbors, we return visited as a potential longest path
    if not has_neighbor:
        return visited

    # iterate over neighbors
    temp = []
    for i in range(n):
        if G[current][i] != 0 and i != current and i not in visited:
            # include i in the list of disited and continue searching further
            visited.append(i)

            # Here we need to use a copy of the array, since it was just referencing visited.
            # FUCK PYTHON'S PASS BY REFERENCE
            temp.append(copy(dfs(G, i, visited)))
            visited.pop()

    
    print(temp)    
    return max(temp, key=len)

if __name__ == "__main__":

    # initialize graph and weights for n vertex graph
    n = 4
    # G = [[randint(0, 1) for i in range(n)] for j in range(n)]
    # G = [[0, 0, 1, 1], [1, 0, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0]]
    G = [[0 for i in range(10)] for j in range(10)]

    for i in range(9):
        G[i][i+1] = 1

    # remove loops
    for i in range(n):
        G[i][i] = 0
    print(G)
    print(dfs(G))
