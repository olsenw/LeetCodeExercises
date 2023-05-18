# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a directed acyclic graph, with n vertices numbered from 0 to n - 1,
    and an array edges where edges[i] = [fromi, toi] represents a directed edge
    from node fromi to node toi.

    Find the smallest set of vertices from which all nodes in the graph are
    reachable. Test cases are written to guarantee a unique solution.

    The vertices can be returned in any order.
    '''
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        # g = {i:[] for i in range(n)}
        v = {i for i in range(n)}
        for a,b in edges:
            # g[a].append(b)
            if b in v:
                v.remove(b)
        return list(v)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 6
        j = [[0,1],[0,2],[2,5],[3,4],[4,2]]
        o = [0,3]
        self.assertEqual(s.findSmallestSetOfVertices(i,j), o)

    def test_two(self):
        s = Solution()
        i = 5
        j = [[0,1],[2,1],[3,1],[1,4],[2,4]]
        o = [0,2,3]
        self.assertEqual(s.findSmallestSetOfVertices(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)