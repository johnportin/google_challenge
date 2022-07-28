from collections import deque

class Node:
    def __init__(self, name, neighbors = [], mate = None):
        """Create a node

        Keyword arguments:
        name -- unique identifier of the vertex
        neighbors -- list of all adjacent nodes
        mate -- the unique mate used for the blossom algorithm
        """
        self.id = name
        self.neighbors = []
        self.mate = mate

        for nbhr in neighbors:
            self.add_neighbor(nbhr)

    def add_neighbor(self, nbhr):
        if nbhr not in self.neighbors:
            self.neighbors.append(nbhr)
        


class Graph:
    def __init__(self, dict = {}):
        """Create a graph from a dictionary representation
        
        Keyword arguments:
        dict -- A dictionary representing the graph. ex: {A: [B, C], B: [A], C:[A]}

        Class variables:
        vertices -- a dictionary of vertices: node pairs matching each 
            vertex name to the corresponding node object
        """
        # for node in dict:
        self.vertices = {}

    def __str__(self):
        result = ""
        for vertex in self.vertices:
            result += str(self.vertices[vertex].id) + " --> " + str(self.vertices[vertex].neighbors) + "\n"

        return result
        

    def add_vertex(self, id):
        if id not in self.vertices:
            # node = Node(id)
            self.vertices[id] = Node(id)
        else:
            return None

    def add_edge(self, v, w):
        if v not in self.vertices:
            self.add_vertex(v)
        if w not in self.vertices:
            self.add_vertex(w)

        self.vertices[v].add_neighbor(w)
        self.vertices[w].add_neighbor(v)
        

    def contract(self, S):
        pass

    def expand(self, S):
        pass

    def bfs(self, start, end):
        visited = []
        queue = deque()
        queue.append([start])

        while queue:
            curr_path = queue.popleft()
            curr_node = curr_path[-1]

            if curr_node not in visited:
                visited.append(curr_node)

                if curr_node == end:
                    print("Found the shortest path!")
                    return curr_path 
                else:
                    for nbhr in self.vertices[curr_node].neighbors:
                        queue.append(curr_path + [nbhr])

        return []

    def distance(self, start, end):
        return len(self.bfs(start, end)) - 1



if __name__ == "__main__":
    G = Graph()
    G.add_edge('a', 'b')
    G.add_edge('b', 'c')
    G.add_edge('a', 'c')
    G.add_edge('b', 'd')
    G.add_edge('d', 'e')
    print(G)

    print(G.distance('e', 'a'))


