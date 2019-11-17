from util import Stack, Queue

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        if vertex not in self.vertices:
            self.vertices[vertex] = set()
        else:
            return False

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise KeyError("That vertex does not exist")


def earliest_ancestor(ancestors, starting_node):
    ancestor_graph = Graph()
    for twin_pair in ancestors:
        ancestor_graph.add_vertex(twin_pair[0])
        ancestor_graph.add_vertex(twin_pair[1])
        ancestor_graph.add_edge(twin_pair[1], twin_pair[0])

    q = Queue()
    q.enqueue([starting_node])

    longest_path = 1
    earliest_ancestor = -1

    while q.size() > 0:
        road = q.dequeue()
        node = road[-1]
        if ((len(road) > longest_path) or
                (len(road) == longest_path and node < earliest_ancestor)):
            earliest_ancestor = node
            longest_path = len(road)
        for neighbor in ancestor_graph.vertices[node]:
            road_copy = list(road)
            road_copy.append(neighbor)
            q.enqueue(road_copy)
    return earliest_ancestor



test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

print(earliest_ancestor(test_ancestors, 11))
