from util import Queue

class AncestorGraph():
    def __init__(self):
        self.vertices = {}

    def add_node(self, node):
        self.vertices[node] = {
            "parents": set(),
            "children": set()
        }

    def add_edge(self, parent, child):
        self.vertices[parent]["children"].add(child)
        self.vertices[child]["parents"].add(parent)

    def get_node(self, node):
        if node in self.vertices:
            return True
        else:
            return False


def earliest_ancestor(ancestors, starting_node):
    graph = AncestorGraph()
    for (parent, child) in ancestors:
        if graph.get_node(parent) == False:
            graph.add_node(parent)
        if graph.get_node(child) == False:
            graph.add_node(child)
        graph.add_edge(parent, child)

    # initialize path array and visited set
    # going to need path's length to see which one has the earlier ancestor
    path = [starting_node]
    visited = set()
    visited.add(starting_node)

    # initialize queue with path
    queue = Queue()
    queue.enqueue(path)

    # initialize generation gap and earliest id to compare to later on
    generation_gap = 0
    earliest_id = None

    # keep running loop until queue is empty
    while queue.size() != 0:
        current_path = queue.dequeue()

        # if the last node does not have any parents
        if len(graph.vertices[current_path[-1]]["parents"]) == 0:
            current_generation_gap = len(current_path) - 1
            # if the `current_generation_gap` is the same as the `generation_gap` stored
            # save the id with the smaller value
            if current_generation_gap == generation_gap:
                if earliest_id == None:
                    earliest_id = current_path[-1]
                elif earliest_id != None and current_path[-1] < earliest_id:
                    earliest_id = current_path[-1]
            # if the `current_generation_gap` is larger than the `generation_gap` stored
            # save the id and corresponding generation_gap
            elif current_generation_gap > generation_gap:
                earliest_id = current_path[-1]
                generation_gap = current_generation_gap
        # continue to add parents to current path and enqueue all available paths
        else:
            for parent in graph.vertices[current_path[-1]]["parents"]:
                queue.enqueue(current_path + [parent])

    # if `earliest_id` is still the same as the `starting_node`, return -1
    if earliest_id == starting_node:
        return -1
    return earliest_id