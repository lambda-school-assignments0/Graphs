# Guided Project - Ancestor

class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, node):
        if node not in self.nodes:
            self.nodes[node] = set()

    def add_edge(self, child, parent):
        self.nodes[child].add(parent)

    def getNeighbors(self, child):
        return self.nodes[child]

class Stack:
    def __init__(self):
        self.storage = []

    def pop(self):
        if self.size() > 0:
            return self.storage.pop()
        else:
            return None

    def push(self, item):
        return self.storage.append(item)

    def size(self):
        return len(self.storage)

def dft(graph, starting_node):
    stack = Stack()

    stack.push((starting_node, 0))
    visited = set()

    visited_pairs = set()

    while stack.size() > 0:
        current_node, current_distance = stack.pop()
        visited_pairs.add((current_node, current_distance))

        if current_node not in visited:
            visited.add(current_node)

            parents = graph.getNeighbors(current_node)

            for parent in parents:
                parent_distance = current_distance + 1
                stack.push((parent, parent_distance))

    longest_distance = 0
    aged_one = -1
    for pair in visited_pairs:
        node = pair[0]
        distance = pair[1]
        if distance > longest_distance:
            longest_distance = distance
            aged_one = node
        if distance == longest_distance:
            if node < aged_one:
                aged_one = node

    return aged_one



def earliest_ancestor(ancestors, starting_node):
    # build graph
    graph = Graph()
    for parent, child in ancestors:
        graph.add_node(child)
        graph.add_node(parent)
        graph.add_edge(child, parent)

    # choose the most distant ancestor
    ## run dft but track each path, then choose the longest path
    ## run dft but add each node as a tuple (node, distance)
    aged_one = dft(graph, starting_node)
    return aged_one