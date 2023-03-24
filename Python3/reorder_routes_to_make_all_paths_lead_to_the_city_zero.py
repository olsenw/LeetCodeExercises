# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import deque
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    There are n cities numbered from 0 to n - 1 and n - 1 roads such that there
    is only one way to travel between two different cities (this network form a
    tree). Last year, the ministry of transport decided to orient the roads in
    one direction because they are too narrow.

    Roads are represented by connections where connections[i] = [ai, bi]
    represents a road from city ai to city bi.

    This year, there will be a big event in the capital (city 0), and many
    people want to travel to this city.

    Reorient the minimum number of roads such that each city can visit city 0.

    It is guaranteed that each city can reach city 0 after reorder.
    '''
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = {i:[] for i in range(n)}
        for i,(j,k) in enumerate(connections):
            graph[j].append(i)
            graph[k].append(i)
        answer = 0
        visited = set()
        q = deque([0])
        while q:
            city = q.popleft()
            visited.add(city)
            for i in graph[city]:
                a,b = connections[i]
                if a == city:
                    if b not in visited:
                        answer += 1
                        q.append(b)
                else:
                    if a not in visited:
                        q.append(a)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 6
        j = [[0,1],[1,3],[2,3],[4,0],[4,5]]
        o = 3
        self.assertEqual(s.minReorder(i,j), o)

    def test_two(self):
        s = Solution()
        i = 5
        j = [[1,0],[1,2],[3,2],[3,4]]
        o = 2
        self.assertEqual(s.minReorder(i,j), o)

    def test_three(self):
        s = Solution()
        i = 3
        j = [[1,0],[2,0]]
        o = 0
        self.assertEqual(s.minReorder(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)