# Course: CS261 - Data Structures
# Author: Kaewan Gardi
# Assignment: 6
# Description:

import heapq
from collections import deque

class DirectedGraph:
    """
    Class to implement directed weighted graph
    - duplicate edges not allowed
    - loops not allowed
    - only positive edge weights
    - vertex names are integers
    """

    def __init__(self, start_edges=None):
        """
        Store graph info as adjacency matrix
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.v_count = 0
        self.adj_matrix = []

        # populate graph with initial vertices and edges (if provided)
        # before using, implement add_vertex() and add_edge() methods
        if start_edges is not None:
            v_count = 0
            for u, v, _ in start_edges:
                v_count = max(v_count, u, v)
            for _ in range(v_count + 1):
                self.add_vertex()
            for u, v, weight in start_edges:
                self.add_edge(u, v, weight)

    def __str__(self):
        """
        Return content of the graph in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if self.v_count == 0:
            return 'EMPTY GRAPH\n'
        out = '   |'
        out += ' '.join(['{:2}'.format(i) for i in range(self.v_count)]) + '\n'
        out += '-' * (self.v_count * 3 + 3) + '\n'
        for i in range(self.v_count):
            row = self.adj_matrix[i]
            out += '{:2} |'.format(i)
            out += ' '.join(['{:2}'.format(w) for w in row]) + '\n'
        out = f"GRAPH ({self.v_count} vertices):\n{out}"
        return out

    # ------------------------------------------------------------------ #

    def add_vertex(self) -> int:
        """
        TODO: Write this implementation
        """
        # Add first index
        if len(self.adj_matrix) < 1:
            self.adj_matrix.append([0])
            self.v_count += 1
            return self.v_count

        # Add 1 more row/column
        self.adj_matrix.append([0] * self.v_count)
        for row in self.adj_matrix:
            row.append(0)

        self.v_count += 1
        return self.v_count

    def add_edge(self, src: int, dst: int, weight=1) -> None:
        """
        TODO: Write this implementation
        """
        # Check inputs
        if src == dst:
            return
        if src < 0 or dst < 0:
            return
        if src >= self.v_count or dst >= self.v_count:
            return
        if weight <= 0:
            return

        self.adj_matrix[src][dst] = weight

    def remove_edge(self, src: int, dst: int) -> None:
        """
        TODO: Write this implementation
        """
        # Check inputs
        if src == dst:
            return
        if src < 0 or dst < 0:
            return
        if src >= self.v_count or dst >= self.v_count:
            return
        if self.adj_matrix[src][dst] == 0:
            return

        self.adj_matrix[src][dst] = 0

    def get_vertices(self) -> []:
        """
        TODO: Write this implementation
        """
        return list(range(self.v_count))

    def get_edges(self) -> []:
        """
        TODO: Write this implementation
        """
        edges = []

        for src in range(len(self.adj_matrix)):
            for dst in range(len(self.adj_matrix[src])):
                if self.adj_matrix[src][dst] > 0:
                    edges.append((src, dst, self.adj_matrix[src][dst]))

        return edges

    def is_valid_path(self, path: []) -> bool:
        """
        TODO: Write this implementation
        """
        # Check path of len 0 and 1
        if len(path) == 0:
            return True

        if len(path) == 1:
            if 0 <= path[0] < self.v_count:
                return True
            else:
                return False

        # Check longer paths
        dst = path[0]
        p_index = 1
        while p_index < len(path):
            src = dst
            dst = path[p_index]
            p_index += 1

            # Check vertices exist
            if src < 0 or dst < 0:
                return False
            if src >= self.v_count or dst >= self.v_count:
                return False

            # Check share an edge
            if self.adj_matrix[src][dst] == 0:
                return False

        return True

    def dfs(self, v_start, v_end=None) -> []:
        """
        TODO: Write this implementation
        """
        visited = set()
        stack = []
        path = []

        # Check start exists
        if v_start >= self.v_count:
            return path

        # Check if end exists
        if v_end and v_end >= self.v_count:
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
                neighbors = [vertex for vertex in range(len(self.adj_matrix[v])) if self.adj_matrix[v][vertex] > 0]
                neighbors.sort()
                for index in range(len(neighbors) - 1, -1, -1):
                    stack.append(neighbors[index])

                path.append(v)

        return path



    def bfs(self, v_start, v_end=None) -> []:
        """
        TODO: Write this implementation
        """
        visited = set()
        queue = deque()
        path = []

        # Check start exists
        if v_start >= self.v_count:
            return path

        # Check if end exists
        if v_end and v_end >= self.v_count:
            v_end = None

        # Do BFS
        queue.append(v_start)
        while queue:
            v = queue.popleft()

            # Is this v_end?
            if v is v_end:
                path.append(v)
                return path

            if v not in visited:
                visited.add(v)

                # Push each to queue in lexicographic
                neighbors = [vertex for vertex in range(len(self.adj_matrix[v])) if self.adj_matrix[v][vertex] > 0]
                neighbors.sort()
                for index in range(len(neighbors)):
                    if neighbors[index] not in visited:
                        queue.append(neighbors[index])

                path.append(v)

        return path

    def has_cycle(self):
        """
        TODO: Write this implementation
        """
        pass

    def dijkstra(self, src: int) -> []:
        """
        TODO: Write this implementation
        """
        # Initialize list of travel costs
        distances = [float('inf')] * self.v_count

        queue = []
        heapq.heapify(queue)

        # Items added to queue as (distance, vertex)
        heapq.heappush(queue, (0, src))

        while queue:
            d, v = heapq.heappop(queue)

            # Check vertex not visited
            if distances[v] == float('inf'):
                # Add v to visited
                distances[v] = d

                # Add neighbors to queue
                neighbors = [vertex for vertex in range(len(self.adj_matrix[v])) if self.adj_matrix[v][vertex] > 0]
                for neighbor in neighbors:
                    delta_d = self.adj_matrix[v][neighbor]
                    new_d = d + delta_d
                    heapq.heappush(queue, (new_d, neighbor))

        return distances


if __name__ == '__main__':

    # print("\nPDF - method add_vertex() / add_edge example 1")
    # print("----------------------------------------------")
    # g = DirectedGraph()
    # print(g)
    # for _ in range(5):
    #     g.add_vertex()
    # print(g)
    #
    # edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
    #          (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    # for src, dst, weight in edges:
    #     g.add_edge(src, dst, weight)
    # print(g)


    # print("\nPDF - method get_edges() example 1")
    # print("----------------------------------")
    # g = DirectedGraph()
    # print(g.get_edges(), g.get_vertices(), sep='\n')
    # edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
    #          (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    # g = DirectedGraph(edges)
    # print(g.get_edges(), g.get_vertices(), sep='\n')
    #
    #
    # print("\nPDF - method is_valid_path() example 1")
    # print("--------------------------------------")
    # edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
    #          (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    # g = DirectedGraph(edges)
    # test_cases = [[0, 1, 4, 3], [1, 3, 2, 1], [0, 4], [4, 0], [], [2]]
    # for path in test_cases:
    #     print(path, g.is_valid_path(path))


    # print("\nPDF - method dfs() and bfs() example 1")
    # print("--------------------------------------")
    # edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
    #          (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    # g = DirectedGraph(edges)
    # for start in range(5):
    #     print(f'{start} DFS:{g.dfs(start)} BFS:{g.bfs(start)}')


    # print("\nPDF - method has_cycle() example 1")
    # print("----------------------------------")
    # edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
    #          (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    # g = DirectedGraph(edges)
    #
    # edges_to_remove = [(3, 1), (4, 0), (3, 2)]
    # for src, dst in edges_to_remove:
    #     g.remove_edge(src, dst)
    #     print(g.get_edges(), g.has_cycle(), sep='\n')
    #
    # edges_to_add = [(4, 3), (2, 3), (1, 3), (4, 0)]
    # for src, dst in edges_to_add:
    #     g.add_edge(src, dst)
    #     print(g.get_edges(), g.has_cycle(), sep='\n')
    # print('\n', g)
    #
    #
    print("\nPDF - dijkstra() example 1")
    print("--------------------------")
    edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
             (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    g = DirectedGraph(edges)
    for i in range(5):
        print(f'DIJKSTRA {i} {g.dijkstra(i)}')
    g.remove_edge(4, 3)
    print('\n', g)
    for i in range(5):
        print(f'DIJKSTRA {i} {g.dijkstra(i)}')
