# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import deque
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    There are n cities. Some of them are connected, while some are not. If city
    a is connected directly with city b, and city b is connected directly with
    city c, them city a is connected indirectly with city c.

    A province is a group of directly or indirectly connected cites and no other
    cites outside the group.

    Given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith
    city and the jth city are directly connected, and isConnected[i][j] = 0 
    otherwise.

    Return the total number of provinces.
    '''
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        a = 0
        v = set()
        for i in range(len(isConnected)):
            if i not in v:
                a += 1
            q = deque([i])
            while q:
                j = q.popleft()
                if j in v:
                    continue
                v.add(j)
                for k in range(len(isConnected)):
                    if isConnected[j][k] and k not in v:
                        q.append(k)
        return a

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,1,0],[1,1,0],[0,0,1]]
        o = 2
        self.assertEqual(s.findCircleNum(i), o)

    def test_two(self):
        s = Solution()
        i = [[1,0,0],[0,1,0],[0,0,1]]
        o = 3
        self.assertEqual(s.findCircleNum(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)