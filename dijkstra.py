""" Implement Dijkstra's algorithm to find shortest path between
    two nodes in graph.
"""
import unittest


def shortest_path(node1, node2, graph, visited=None):
    if not node1 or not node2 or not graph or node1 not in graph or node2 not in graph:
        return
    if visited is None:
        visited = []
    graph[node1]['weight'] = 0

    for node in graph:
        for adj_node in graph[node]['adjacent']:
            if adj_node in visited:
                continue
            if (
                graph[adj_node]['weight']
                > graph[node]['weight'] + graph[node]['adjacent'][adj_node]
            ):
                graph[adj_node]['weight'] = (
                    graph[node]['weight'] + graph[node]['adjacent'][adj_node]
                )
        visited.append(node)

    return graph[node2]['weight']


class TestShortestPath(unittest.TestCase):
    def setUp(self):
        INFINITY = 9999999
        # https://www.youtube.com/watch?v=CL1byLngb5Q
        self.graph = {
            'A': {'weight': INFINITY, 'adjacent': {'B': 2, 'C': 4}},
            'B': {'weight': INFINITY, 'adjacent': {'A': 2, 'C': 1, 'D': 4, 'E': 2}},
            'C': {'weight': INFINITY, 'adjacent': {'A': 4, 'B': 1, 'E': 3}},
            'D': {'weight': INFINITY, 'adjacent': {'B': 4, 'E': 3, 'F': 2}},
            'E': {'weight': INFINITY, 'adjacent': {'B': 2, 'C': 3, 'D': 3, 'F': 2}},
            'F': {'weight': INFINITY, 'adjacent': {'D': 2, 'E': 2}},
        }

    def test_shortest_path(self):
        self.assertEqual(shortest_path('A', 'F', self.graph), 6)
        self.assertEqual(shortest_path('A', 'E', self.graph), 4)