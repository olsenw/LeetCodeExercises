# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

from collections import defaultdict, deque

class Solution:
    '''
    Given an array of variable pairs equations and an array of real
    numbers values, where equations[i] = [ai,bi] and values[i] represent
    the equation ai / bi = values[i]. Each ai or bi is a string that
    represents a single variable.

    There is also given an array queries, where queries[j] = [cj, dj]
    represents the jth query where you must find the answer for
    cj / dj = ?.

    Return the answers to all queries. If a single answer cannot be
    determined, return -1.0.

    Note: the input is always valid. It is assumed that evaluating the
    queries will not result in division by zero and that there is no
    contradiction.
    '''
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # create graph
        graph = defaultdict(list)
        for [i, j], k in zip(equations, values):
            graph[i].append((j, k))
            graph[j].append((i, 1 / k))
        # function to search the graph
        def search(start, target):
            d = deque([(start, 1.0)])
            v = {start}
            while d:
                n, w = d.popleft()
                if n == target:
                    return w
                for i, j in graph[n]:
                    if i not in v:
                        v.add(i)
                        d.append((i, j * w))
            return -1.0
        # solve all queries if possible
        ans = []
        for i,j in queries:
            if i not in graph or j not in graph:
                ans.append(-1.0)
            # find a path from node i to j multiplying along the way
            else:
                ans.append(search(i,j))
        return ans

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [["a","b"],["b","c"]]
        j = [2.0,3.0]
        k = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
        o = [6.00000,0.50000,-1.00000,1.00000,-1.00000]
        self.assertEqual(s.calcEquation(i,j,k), o)

    def test_two(self):
        s = Solution()
        i = [["a","b"],["b","c"],["bc","cd"]]
        j = [1.5,2.5,5.0]
        k = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
        o = [3.75000,0.40000,5.00000,0.20000]
        self.assertEqual(s.calcEquation(i,j,k), o)

    def test_three(self):
        s = Solution()
        i = [["a","b"]]
        j = [0.5]
        k = [["a","b"],["b","a"],["a","c"],["x","y"]]
        o = [0.50000,2.00000,-1.00000,-1.00000]
        self.assertEqual(s.calcEquation(i,j,k), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)