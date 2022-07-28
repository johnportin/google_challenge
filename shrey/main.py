from mimetypes import init


def solution(l):
    g = generate_graph(l)
    matches = reduce(g)
    return len(l) - matches

def loop(x,y):
    base = int((x+y)/gcd(x,y))
    return bool(base & (base - 1))

def gcd(a,b):
    while b:
        a, b = b, a % b
    return a

def generate_graph(l):
    G = {i: [] for i in range(len(l))}
    for i in range(len(l)):
        for j in range(i, len(l)):
            if i != j and loop(l[i], l[j]):
                G[i].append(j)
                G[j].append(i)
    return G

def reduce(g):
    for row in g:
        print(g[row])
    matched = 0
    checks = len(g[max(g, key=lambda key: len(g[key]))])
    print("checks = {}".format(checks))
    while len(g) > 1 and checks >= 1:
        print("-" * 40)
        init_mw_node = min(g, key=lambda key: len(g[key]))
        print("init node = {}".format(init_mw_node))
        for row in g:
            print("{}: {}".format(row, g[row]))
        if (len(g[init_mw_node])) < 1 :
            del g[init_mw_node]
        else:
            temp_sec_min = [len(g[g[init_mw_node][0]])+1,1]
            print("temp sec min = {}".format(temp_sec_min))
            # We are going to match the init node.
            # Looking for adjacent node with least degree
            # Removing init node from their list of edges along the way
            for node_i in g[init_mw_node]:
                if len(g[node_i]) < temp_sec_min[0]:
                    temp_sec_min = [len(g[node_i]), node_i]

                for check_i in range(len(g[node_i])):
                    if g[node_i][check_i] == init_mw_node:
                        print("Deleting {} at node = {}, check = {} since it == {}". format(g[node_i][check_i], node_i, check_i, init_mw_node))
                        del g[node_i][check_i]
                        break
            for node_i in g[temp_sec_min[1]]:
                for check_i in range(len(g[node_i])):
                    if g[node_i][check_i] == temp_sec_min[1]:
                        print("deleting at node = {}, check = {}, term = {}".format(node_i, check_i, g[node_i][check_i]))
                        del g[node_i][check_i]
                        break
            print("deleting {} at {} and {} at {}".format(g[init_mw_node], init_mw_node, g[temp_sec_min[1]], temp_sec_min[1]))
            del g[init_mw_node]
            del g[temp_sec_min[1]]
            matched += 2
        if len(g) > 1:
            print("Checks = {}".format(checks))
            checks = len(g[max(g, key=lambda key: len(g[key]))])
    return matched

if __name__ == "__main__":
    print(solution([1, 7, 3, 21, 13, 19, 4]))