# Course: CS261 - Data Structures
# Author: Kaewan Gardi
# Assignment: 6
# Description:

from collections import deque

class UndirectedGraph:
    """
    Class to implement undirected graph
    - duplicate edges not allowed
    - loops not allowed
    - no edge weights
    - vertex names are strings
    """

    def __init__(self, start_edges=None):
        """
        Store graph info as adjacency list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.adj_list = dict()

        # populate graph with initial vertices and edges (if provided)
        # before using, implement add_vertex() and add_edge() methods
        if start_edges is not None:
            for u, v in start_edges:
                self.add_edge(u, v)

    def __str__(self):
        """
        Return content of the graph in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = [f'{v}: {self.adj_list[v]}' for v in self.adj_list]
        out = '\n  '.join(out)
        if len(out) < 70:
            out = out.replace('\n  ', ', ')
            return f'GRAPH: {{{out}}}'
        return f'GRAPH: {{\n  {out}}}'

    # ------------------------------------------------------------------ #

    def add_vertex(self, v: str) -> None:
        """
        Add new vertex to the graph
        """
        # Check vertex already in graph
        if v in self.adj_list:
            return

        # Create new vertex
        self.adj_list[v] = []

    def add_edge(self, u: str, v: str) -> None:
        """
        Add edge to the graph
        """
        if v == u:
            return

        # Ensure vertices exist
        if u not in self.adj_list:
            self.add_vertex(u)
        if v not in self.adj_list:
            self.add_vertex(v)

        if v not in self.adj_list[u]:
            self.adj_list[u].append(v)

        if u not in self.adj_list[v]:
            self.adj_list[v].append(u)

    def remove_edge(self, v: str, u: str) -> None:
        """
        Remove edge from the graph
        """
        # Check vertices exist
        if v not in self.adj_list or u not in self.adj_list:
            return

        # Remove the edge
        if u in self.adj_list[v]:
            self.adj_list[v].remove(u)
        if v in self.adj_list[u]:
            self.adj_list[u].remove(v)

    def remove_vertex(self, v: str) -> None:
        """
        Remove vertex and all connected edges
        """
        # Check vertex exists
        if v not in self.adj_list:
            return

        to_remove = self.adj_list.pop(v)

        # Remove all edges connected to v
        for vertex in to_remove:
            if v in self.adj_list[vertex]:
                self.adj_list[vertex].remove(v)

    def get_vertices(self) -> []:
        """
        Return list of vertices in the graph (any order)
        """
        return [key for key in self.adj_list]

    def get_edges(self) -> []:
        """
        Return list of edges in the graph (any order)
        """
        edges = []

        # Add all edges to list
        for vertex in self.adj_list:
            for neighbor in self.adj_list[vertex]:

                # Exclude duplicate edges
                if (neighbor, vertex) not in edges:
                    edges.append((vertex, neighbor))

        return edges

    def is_valid_path(self, path: []) -> bool:
        """
        Return true if provided path is valid, False otherwise
        """
        last = None

        # Traverse path
        for vertex in path:
            # Check vertex exists
            if vertex not in self.adj_list:
                return False

            # First vertex
            if not last:
                last = vertex

            # Continue path
            elif vertex in self.adj_list[last]:
                last = vertex

            # Disconnected
            else:
                return False

        # Path verifies
        return True

    def dfs(self, v_start, v_end=None) -> []:
        """
        Return list of vertices visited during DFS search
        Vertices are picked in alphabetical order
        """
        visited = set()
        stack = []
        path = []

        # Check start exists
        if v_start not in self.adj_list:
            return path

        # Check if end exists
        if v_end and v_end not in self.adj_list:
            v_end = None

        # Do DFS
        stack.append(v_start)
        while stack:
            v = stack.pop()

            # Is this v_end?
            if v is v_end:
                path.append(v)
                return path

            # Have not visited v
            if v not in visited:
                visited.add(v)

                # Push each to stack in reverse lexicographic
                self.adj_list[v].sort()
                for neighbor in range(len(self.adj_list[v]) - 1, -1, -1):
                    stack.append(self.adj_list[v][neighbor])
                path.append(v)

        return path

    def bfs(self, v_start, v_end=None) -> []:
        """
        Return list of vertices visited during BFS search
        Vertices are picked in alphabetical order
        """
        visited = set()
        queue = []
        path = []

        # Check start exists
        if v_start not in self.adj_list:
            return path

        # Check if end exists
        if v_end and v_end not in self.adj_list:
            v_end = None

        # Do BFS
        queue.append(v_start)
        while queue:
            v = queue.pop(0)

            # Is this v_end?
            if v is v_end:
                path.append(v)
                return path

            if v not in visited:
                visited.add(v)

                # Push each to queue in lexicographic
                self.adj_list[v].sort()
                for neighbor in range(len(self.adj_list[v])):
                    if self.adj_list[v][neighbor] not in visited:
                        queue.append(self.adj_list[v][neighbor])
                path.append(v)

        return path

    def count_connected_components(self):
        """
        Return number of connected componets in the graph
        """
        vertex_list = self.get_vertices()
        connected_count = 0

        # Find each connected component and increment count
        while vertex_list:
            connected = self.bfs(vertex_list[0])
            connected_count += 1
            for v in connected:
                vertex_list.remove(v)

        return connected_count

    def has_cycle(self):
        """
        Return True if graph contains a cycle, False otherwise
        """


        # # Look for a cycle
        # for vertex in self.adj_list:
        #     if self.is_cycle(vertex, set()):
        #         return True
        #
        # return False

    def is_cycle(self, v_start, visited):
        """
        Detects if there is a cycle starting and ending at the given vertex
        """
        visited.add(v_start)








   


if __name__ == '__main__':

    # print("\nPDF - method add_vertex() / add_edge example 1")
    # print("----------------------------------------------")
    # g = UndirectedGraph()
    # print(g)
    #
    # for v in 'ABCDE':
    #     g.add_vertex(v)
    # print(g)
    #
    # g.add_vertex('A')
    # print(g)
    #
    # for u, v in ['AB', 'AC', 'BC', 'BD', 'CD', 'CE', 'DE', ('B', 'C')]:
    #     g.add_edge(u, v)
    # print(g)

    #
    # print("\nPDF - method remove_edge() / remove_vertex example 1")
    # print("----------------------------------------------------")
    # g = UndirectedGraph(['AB', 'AC', 'BC', 'BD', 'CD', 'CE', 'DE'])
    # g.remove_vertex('DOES NOT EXIST')
    # g.remove_edge('A', 'B')
    # g.remove_edge('X', 'B')
    # print(g)
    # g.remove_vertex('D')
    # print(g)

    #
    # print("\nPDF - method get_vertices() / get_edges() example 1")
    # print("---------------------------------------------------")
    # g = UndirectedGraph()
    # print(g.get_edges(), g.get_vertices(), sep='\n')
    # g = UndirectedGraph(['AB', 'AC', 'BC', 'BD', 'CD', 'CE'])
    # print(g.get_edges(), g.get_vertices(), sep='\n')

    #
    # print("\nPDF - method is_valid_path() example 1")
    # print("--------------------------------------")
    # g = UndirectedGraph(['AB', 'AC', 'BC', 'BD', 'CD', 'CE', 'DE'])
    # test_cases = ['ABC', 'ADE', 'ECABDCBE', 'ACDECB', '', 'D', 'Z']
    # for path in test_cases:
    #     print(list(path), g.is_valid_path(list(path)))


    # print("\nPDF - method dfs() and bfs() example 1")
    # print("--------------------------------------")
    # edges = ['AE', 'AC', 'BE', 'CE', 'CD', 'CB', 'BD', 'ED', 'BH', 'QG', 'FG']
    # g = UndirectedGraph(edges)
    # test_cases = 'ABCDEGH'
    # for case in test_cases:
    #     print(f'{case} DFS:{g.dfs(case)} BFS:{g.bfs(case)}')
    # print('-----')
    # for i in range(1, len(test_cases)):
    #     v1, v2 = test_cases[i], test_cases[-1 - i]
    #     print(f'{v1}-{v2} DFS:{g.dfs(v1, v2)} BFS:{g.bfs(v1, v2)}')

    #
    # print("\nPDF - method count_connected_components() example 1")
    # print("---------------------------------------------------")
    # edges = ['AE', 'AC', 'BE', 'CE', 'CD', 'CB', 'BD', 'ED', 'BH', 'QG', 'FG']
    # g = UndirectedGraph(edges)
    # test_cases = (
    #     'add QH', 'remove FG', 'remove GQ', 'remove HQ',
    #     'remove AE', 'remove CA', 'remove EB', 'remove CE', 'remove DE',
    #     'remove BC', 'add EA', 'add EF', 'add GQ', 'add AC', 'add DQ',
    #     'add EG', 'add QH', 'remove CD', 'remove BD', 'remove QG')
    # for case in test_cases:
    #     command, edge = case.split()
    #     u, v = edge
    #     g.add_edge(u, v) if command == 'add' else g.remove_edge(u, v)
    #     print(g.count_connected_components(), end=' ')
    # print()


    print("\nPDF - method has_cycle() example 1")
    print("----------------------------------")
    edges = ['AE', 'AC', 'BE', 'CE', 'CD', 'CB', 'BD', 'ED', 'BH', 'QG', 'FG']
    g = UndirectedGraph(edges)
    test_cases = (
        'add QH', 'remove FG', 'remove GQ', 'remove HQ',
        'remove AE', 'remove CA', 'remove EB', 'remove CE', 'remove DE',
        'remove BC', 'add EA', 'add EF', 'add GQ', 'add AC', 'add DQ',
        'add EG', 'add QH', 'remove CD', 'remove BD', 'remove QG',
        'add FG', 'remove GE')
    for case in test_cases:
        command, edge = case.split()
        u, v = edge
        g.add_edge(u, v) if command == 'add' else g.remove_edge(u, v)
        print('{:<10}'.format(case), g.has_cycle())
