"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # initialize queue with starting_vertex
        queue = Queue()
        queue.enqueue(starting_vertex)

        # initialize path taken and visited dictionary (sets do not usually preserve order)
        path = []
        visited = set()

        # keep running loop until queue is empty
        while queue.size() != 0:
            current_node = queue.dequeue()

            # prevent infinite looping
            if current_node not in visited:
                path.append(current_node)
                visited.add(current_node)
            
                # add neighbors of current_node to queue
                for vertex in self.get_neighbors(current_node):
                    queue.enqueue(vertex)
        
        return path

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # initialize stack with starting vertex
        stack = Stack()
        stack.push(starting_vertex)

        # initialize path taken and visited dictionary (sets do not usually preserve order)
        path = []
        visited = set()

        # keep running loop until stack is empty
        while stack.size() != 0:
            current_node = stack.pop()

            # prevent infinite looping
            if current_node not in visited:
                path.append(current_node)
                visited.add(current_node)

                # add neighbors of current_node to stack
                for vertex in self.get_neighbors(current_node):
                    stack.push(vertex)

        return path

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # define helper function for recursion
        def dft_recursive_helper(starting_vertex, visited = set()):
            if starting_vertex not in visited:
                visited.add(starting_vertex)
                return [starting_vertex] + sum([dft_recursive_helper(vertex, visited) for vertex in self.get_neighbors(starting_vertex)], [])
            else:
                return []

        return dft_recursive_helper(starting_vertex)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # initialize path taken and visited dictionary (sets do not usually preserve order)
        path = [starting_vertex]
        visited = set()
        visited.add(starting_vertex)

        # initialize queue with path
        queue = Queue()
        queue.enqueue(path)

        # keep running loop until queue is empty
        while queue.size() != 0:
            current_path = queue.dequeue()

            if current_path[-1] == destination_vertex:
                return current_path
            
            # add neighbors of current_node to queue
            for vertex in self.get_neighbors(current_path[-1]):
                if vertex not in visited:
                    queue.enqueue(current_path + [vertex])

        return -1

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # initialize path taken and visited dictionary (sets do not usually preserve order)
        path = [starting_vertex]
        visited = set()
        visited.add(starting_vertex)

        # initialize queue with starting_vertex
        stack = Stack()
        stack.push(path)

        # keep running loop until queue is empty
        while stack.size() != 0:
            current_path = stack.pop()

            if current_path[-1] == destination_vertex:
                return current_path
            
            # add neighbors of current_node to stack
            for vertex in self.get_neighbors(current_path[-1]):
                if vertex not in visited:
                    stack.push(current_path + [vertex])

        return -1

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # initialize path and found flag
        path = []
        found = [False]

        # define helper function for recursion
        def dft_recursive_helper(starting_vertex, visited = set()):
            if starting_vertex not in visited and found[0] != True:
                path.append(starting_vertex)
                visited.add(starting_vertex)
                if starting_vertex == destination_vertex:
                    found[0] = True
                for vertex in self.get_neighbors(starting_vertex):
                    dft_recursive_helper(vertex, visited)

        dft_recursive_helper(starting_vertex)
        return path

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)


    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    print(graph.bft(1))

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print(graph.dft(1))
    print(graph.dft_recursive(1))

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
