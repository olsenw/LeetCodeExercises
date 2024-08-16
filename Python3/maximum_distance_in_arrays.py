# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import heapq
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    # O(n^2) 
    def maxDistance_tme(self, arrays: List[List[int]]) -> int:
        answer = 0
        m = len(arrays)
        for i in range(m):
            for j in range(i + 1, m):
                answer = max(
                        answer,
                        abs(arrays[i][0] - arrays[j][-1]),
                        abs(arrays[i][-1] - arrays[j][0])
                    )
        return answer

    def maxDistance_incorrect(self, arrays: List[List[int]]) -> int:
        a,b = [], []
        for i in range(len(arrays)):
            pass
            if len(a) < 2:
                heapq.heappush(a, (-arrays[i][0], i))
            else:
                heapq.heappushpop(a, (-arrays[i][0], i))
            if len(b) < 2:
                heapq.heappush(b, (arrays[i][-1], i))
            else:
                heapq.heappushpop(b, (arrays[i][-1], i))
        if a[1][1] != b[1][1]:
            return abs(-a[1][0] - b[1][0])
        return max(
            abs(-a[0][0] - b[1][1]),
            abs(-a[1][0] - b[0][1]),
            abs(-a[0][0] - b[0][1]),
        )

    # based on solution by Sachinonly_
    # https://leetcode.com/problems/maximum-distance-in-arrays/solutions/5642927/easy-greedy-solution-beats-100/?envType=daily-question&envId=2024-08-16
    def maxDistance(self, arrays: List[List[int]]) -> int:
        small = arrays[0][0]
        large = arrays[0][-1]
        answer = 0
        for i in range(1, len(arrays)):
            answer = max(answer, abs(arrays[i][-1] - small), abs(large - arrays[i][0]))
            small = min(small, arrays[i][0])
            large = max(large, arrays[i][-1])
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,2,3],[4,5],[1,2,3]]
        o = 4
        self.assertEqual(s.maxDistance(i), o)

    def test_two(self):
        s = Solution()
        i = [[1],[1]]
        o = 0
        self.assertEqual(s.maxDistance(i), o)

    def test_three(self):
        s = Solution()
        i = [[3,4],[2,10],[3,4]]
        o = 7
        self.assertEqual(s.maxDistance(i), o)

    def test_four(self):
        s = Solution()
        i = [[1],[2]]
        o = 1
        self.assertEqual(s.maxDistance(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)