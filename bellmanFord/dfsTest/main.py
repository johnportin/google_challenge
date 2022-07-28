def dfs(graph, values, current, visited = [], curr_max = 0):
    n = len(graph)
    if len(visited) == 0:
        visited.append(current)

    # print("comparing {} and {}".format(values[current], curr_max))

    # if values[current] > curr_max:
    #     curr_max = values[current]

    if visited == [0, 1, 2, 3, 4]:
        return -float('inf')

    temp = [curr_max, values[current]]
    for i in range(n):
        if i not in visited and graph[current][i] == 1:
            visited.append(i)
            temp.append(dfs(graph, values, i, visited, curr_max))

        

    print(temp)

    # print("Returning max = {}".format(curr_max))
    if len(temp) > 0:
        return max(temp)
    return []

if __name__ == "__main__":
    print("Running dfs")

    G = [[0, 1, 0, 0, 0], [1, 0, 1, 0, 0], [0, 1, 0, 1, 1], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0]]
    V = {0: 30, 1: 5, 2: 10, 3: 7, 4: 11}
    print(dfs(G, V, 2))