"""Islands problem implementation"""

from collections import deque
import unittest


def _check_neighbor(q, graph, i, j, rows, cols):
    """Add to queue if connected to island."""
    if (i >= 0 and i < rows) and (j >= 0 and j < cols) and (graph[i][j] == 1):
        # Mark visited
        graph[i][j] = 2
        q.appendleft([i, j])


def _check_neighbors(graph, i, j, rows, cols):
    """Check for islands connected to point [i][j] with BFS.
        Set values to `2` to designated visited."""
    q = deque()
    q.appendleft([i, j])

    while q:
        i, j = q.pop()
        _check_neighbor(q, graph, i, j, rows, cols)
        _check_neighbor(q, graph, i + 1, j, rows, cols)
        _check_neighbor(q, graph, i, j + 1, rows, cols)
        _check_neighbor(q, graph, i - 1, j, rows, cols)
        _check_neighbor(q, graph, i, j - 1, rows, cols)



def count_islands(graph):
    """ Return number of `islands` on graph where islands
        are 1s connected horizontally and vertically."""

    if graph is None or graph == [[]]:
        return 0

    rows = len(graph)
    cols = len(graph[0])
    count = 0

    for i in range(rows):
        for j in range(cols):
            if graph[i][j] == 1:
                count += 1
                _check_neighbors(graph, i, j, rows, cols)

    return count


class TestCountIslands(unittest.TestCase):
    def setUp(self):
        self.data = (
            (None, 0),
            ([[]], 0),
            ([[0, 0, 1], [1, 0, 1], [1, 1, 0]], 2),
            ([[1, 0, 0, 0], [1, 1, 1, 1], [0, 1, 0, 1]], 1),
            ([[1, 1, 0], [0, 0, 0], [1, 1, 1], [1, 0, 0]], 2),
            ([[1, 1, 0], [0, 0, 1], [0, 0, 0], [1, 0, 1]], 4)
        )

    def test_count_islands(self):
        for graph, expected in self.data:
            self.assertEqual(count_islands(graph), expected)


if __name__ == '__main__':
    unittest.main()