from random import randint

def dfs(G, W, current = 0, visited = [], temp_max = [], time = 50):
    n = len(G)
    # checking conditions
    

    # iterate over each neighbor
    result = []
    for i in range(n):

        # call dfs for each neighbor
        if G[current][i] != 0 and i not in visited:
            w = W[current][i]
            if time - w >= 0:
                visited.append(i)

                if sum(visited) > sum(temp_max):
                    temp_max = visited
                time -= w
                temp = dfs(G, W, i, visited, temp_max, time)

                if sum(temp) > sum(temp_max):
                    result = temp

                visited.pop()

    # return max value
    return result


if __name__ == "__main__":

    # initialize graph and weights for n vertex graph
    n = 5
    G = [[1 for i in range(n)] for j in range(n)]
    W = [[randint(0, 50) for i in range(n)] for j in range(n)]

    # remove loops
    for i in range(n):
        G[i][i] = 0
        W[i][i] = 0

    print(dfs(G, W, time = 100))

    


