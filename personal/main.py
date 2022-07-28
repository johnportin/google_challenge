from fractions import gcd

def is_solvable(x, y, dict = {}, prev = []):
    # x, y is solvable if and only if x + y == 2^k for some k
    total = x + y
    reduced = total // gcd(x, y)

    return (reduced - 1) & reduced

       
def construct_graph(l):
    k = len(l)
    G = {i: [] for i in range(k)}

    for i in range(k):
        for j in range(i + 1, k):
            if is_solvable(l[i], l[j]):
                G[i].append(j)
                G[j].append(i)
    # for node in G:
    #     print("{}: {}".format(node, G[node]))
    return G

def matching(graph):
    """ Greedy approach to matching:
            1. Find the node with least degree
            2. Find the neighbor with least degree
            3. Remove them from the graph and add to the matching
    """
    M = {}
    G = graph

    lenG = len(G)

    while len(G) > 1:
        curr = min(graph, key= lambda x: len(G[x]))
        if len(G[curr]) < 1:
            del G[curr]
        else:
            temp = [G[G[curr][0]], 0]
            # Find potential candidates for curr
            for nbhr in G[curr]:
                if len(G[nbhr]) < temp[0]:
                    temp = [len(G[nbhr]), nbhr]
                # delete curr from all neighbors of nbhr
                for nbhr2 in range(len(G[nbhr])):
                    if G[nbhr][nbhr2] == curr:
                        del G[nbhr][nbhr2]
                        break # break early after findind matching to avoid index issues

            # after findind the second node to delete, go through and remove that node
            # from each other edge list
            curr2 = temp[1]
            for nbhr in G[curr2]:
                for nbhr2 in range(len(G[nbhr])):
                    if G[nbhr][nbhr2] == curr2:
                        del G[nbhr][nbhr2] # break early to avoid index issues
                        break

            # Finally, delete curr and curr2, and increase the matching
            M[curr] = curr2
            del G[curr]
            del G[curr2]

    return lenG - (len(M) * 2)



if __name__ == "__main__":
    l = [1, 7, 3, 21, 13, 19, 1]
    adj = construct_graph(l)
    print(adj)
    print(matching(adj))