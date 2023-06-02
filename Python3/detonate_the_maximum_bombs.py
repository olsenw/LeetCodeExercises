# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import deque
import math
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a list of bombs. The range of a bomb is defined as the area where its
    effect can be felt. This area is in the shape of a circle with the center as
    the location of the bomb.

    The bombs are represented by a 0-indexed 2D integer array bombs where
    bombs[i] = [xi, yi, ri]. xi and yi denote the X-coordinate and the
    y-coordinate of the location of the ith bomb, whereas ri denotes the radius
    of its range.

    A single bomb is chosen to detonate. When a bomb is detonated, it will
    detonate all bombs that lie in its range. These bombs will further detonate
    the bombs that lie in their ranges.

    Given the list of bombs, return the maximum number of bombs that can be
    detonated by a single starting bomb.
    '''
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        graph = {i:[] for i in range(n)}
        for i in range(n):
            x,y,r = bombs[i]
            for j in range(n):
                a,b,c = bombs[j]
                if i != j and (x-a)**2 + (y-b)**2 <= r**2:
                    graph[i].append(j)
        def bfs(b):
            detonated = set()
            q = deque([b])
            while q:
                i = q.popleft()
                if i in detonated:
                    continue
                detonated.add(i)
                for j in graph[i]:
                    q.append(j)
            return len(detonated)
        return max(bfs(i) for i in range(n))

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[2,1,3],[6,1,4]]
        o = 2
        self.assertEqual(s.maximumDetonation(i), o)

    def test_two(self):
        s = Solution()
        i = [[1,1,5],[10,10,5]]
        o = 1
        self.assertEqual(s.maximumDetonation(i), o)

    def test_three(self):
        s = Solution()
        i = [[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]]
        o = 5
        self.assertEqual(s.maximumDetonation(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)