# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import Counter, defaultdict
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 0-indexed 2D integer array pairs where pairs[i] = [starti, endi]. An
    arrangement of pairs is valid if for every index i where
    1 <= i < pairs.length and endi-1 == starti.

    Return any valid arrangement of pairs.

    Note: The inputs will be generated such that there exists a valid
    arrangement of pairs.
    '''
    # description of Hierholzer's algorithm
    # https://www.geeksforgeeks.org/hierholzers-algorithm-directed-graph/#
    # needed help from Leetcode editorial for finding start point
    # https://leetcode.com/problems/valid-arrangement-of-pairs/?envType=daily-question&envId=2024-11-30
    # this algorithm is magic
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        inDegree = Counter()
        outDegree = Counter()
        for a,b in pairs:
            graph[a].append(b)
            inDegree[b] += 1
            outDegree[a] += 1
        circuit = []
        # curr = [min(graph.keys())]
        curr = []
        for d in outDegree:
            if inDegree[d] < outDegree[d]:
                curr.append(d)
        if not curr:
            curr.append(d)
        pass
        while curr:
            v = curr[-1]
            if graph[v]:
                curr.append(graph[v].pop())
            else:
                circuit.append(curr.pop())
        answer = []
        for i in range(len(circuit)-1,0,-1):
            answer.append([circuit[i], circuit[i-1]])
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[5,1],[4,5],[11,9],[9,4]]
        o = [[11,9],[9,4],[4,5],[5,1]]
        self.assertEqual(s.validArrangement(i), o)

    def test_two(self):
        s = Solution()
        i = [[1,3],[3,2],[2,1]]
        o = [[1,3],[3,2],[2,1]]
        self.assertEqual(s.validArrangement(i), o)

    def test_three(self):
        s = Solution()
        i = [[1,2],[1,3],[2,1]]
        o = [[1,2],[2,1],[1,3]]
        self.assertEqual(s.validArrangement(i), o)

    def test_four(self):
        s = Solution()
        i = [[0,1]]
        o = [[0,1]]
        self.assertEqual(s.validArrangement(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)