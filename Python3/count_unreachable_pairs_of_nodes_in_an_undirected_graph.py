# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import deque
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer n. There is an undirected graph with n nodes, numbered from
    0 to n - 1. Given a 2D integer array edges where edges[i] = [ai, bi] denotes
    that there exists an undirected edge connecting nodes ai and bi.

    Return the number of pairs of different nodes that are unreachable from each
    other.
    '''
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        graph = {i:[] for i in range(n)}
        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)
        unvisited = set(range(n))
        # groups = []
        answer = 0
        while unvisited:
            q = deque([unvisited.pop()])
            unvisited.add(q[0])
            nodes = 0
            while q:
                node = q.popleft()
                if node not in unvisited:
                    continue
                unvisited.remove(node)
                for i in graph[node]:
                    q.append(i)
                nodes += 1
            n -= nodes
            answer += nodes * n
            # groups.append(nodes)
        # return sum(groups[i] * groups[j] for i in range(len(groups) - 1) for j in range(i + 1, len(groups)))
        # answer = 0
        # for i in groups[:-1]:
        #     n -= i
        #     answer += i * n
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 3
        j = [[0,1],[0,2],[1,2]]
        o = 0
        self.assertEqual(s.countPairs(i,j), o)

    def test_two(self):
        s = Solution()
        i = 7
        j = [[0,2],[0,5],[2,4],[1,6],[5,4]]
        o = 14
        self.assertEqual(s.countPairs(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)