import unittest


def dfs_visited_iter(node, graph):
    """DFS: Return visited nodes iterably via stack"""
    stack = [node]
    visited = []
    while stack:
        current = stack.pop()
        if current not in visited:
            visited.append(current)
        stack.extend(graph[current])
    return visited


def dfs_visited_re(node, graph, visited=[]):
    """DFS: Return visited nodes via recursion"""
    for child in graph[node]:
        if child not in visited:
            visited.append(child)
        dfs_visited_re(child, graph, visited)
    return visited


def bfs_visited(node, graph):
    """BFS: Return visited nodes"""
    queue = [node]
    visited = []

    while queue:
        current = queue.pop()
        # Enqueue unvisited neighbors
        queue[0:0] = [
            neighbor for neighbor in graph[current] if neighbor not in visited
        ]
        visited.append(current)
    return visited


def is_path(node1, node2, graph, method):
    """Return True if path between `node1` and `node2`"""
    return node2 in method(node1, graph)


class TestIsPath(unittest.TestCase):
    def setUp(self):
        self.graph1 = {
            'A': ['B', 'D'],
            'B': [],
            'C': [],
            'D': ['E'],
            'E': ['C'],
            'F': ['C'],
        }
        self.graph2 = {
            'A': ['B', 'C', 'E'],
            'B': ['D'],
            'C': [],
            'D': ['G'],
            'E': [],
            'F': ['E', 'C'],
            'G': ['C'],
        }

    def test_is_path_dfs_iter(self):
        self.assertFalse(is_path('A', 'F', self.graph1, dfs_visited_iter))
        self.assertTrue(is_path('A', 'C', self.graph2, dfs_visited_iter))

    def test_is_path_dfs_recursive(self):
        self.assertFalse(is_path('A', 'F', self.graph1, dfs_visited_re))
        self.assertTrue(is_path('A', 'C', self.graph2, dfs_visited_re))

    def test_is_path_bfs(self):
        self.assertFalse(is_path('A', 'F', self.graph1, bfs_visited))
        self.assertTrue(is_path('A', 'C', self.graph2, bfs_visited))


if __name__ == '__main__':
    unittest.main()
