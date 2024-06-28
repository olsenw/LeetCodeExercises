# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import defaultdict
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer n denoting the number of cities in a country. The cities
    are numbered from 0 to n - 1.

    Also given a 2D integer array roads where roads[i] = [ai, bi] denotes that
    theirs exists a bidirectional road connecting cities ai and bi.

    Need to assign each city with an integer value from 1 to n, where each value
    can only be used once. The importance of a road is then defined as the sum
    of the values of the two cities it connects.

    Return the maximum total importance of all roads possible after assigning
    the values optimally.
    '''
    # slow
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a,b in roads:
            graph[a].append(b)
            graph[b].append(a)
        importance = sorted(
            (i for i in graph),
            key=lambda i: (len(graph[i]), max(len(graph[j]) for j in graph[i])),
            reverse=True)
        pass
        graph = {i:j for i,j in zip(importance, range(n, 0, -1))}
        return sum(graph[i] + graph[j] for i,j in roads)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 5
        j = [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]]
        o = 43
        self.assertEqual(s.maximumImportance(i,j), o)

    def test_two(self):
        s = Solution()
        i = 5
        j = [[0,3],[2,4],[1,3]]
        o = 20
        self.assertEqual(s.maximumImportance(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)