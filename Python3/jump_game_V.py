# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an array of integers arr and an integer d. In one step it is possible
    to jump from index i to index:
    * i + x where i + x < arr.length and 0 < x <= d.
    * i - x where i - x >= 0 and 0 < x <= d.

    In addition, it is only possible to jump from index i to index j if
    arr[i] > arr[j] and arr[i] > arr[k] for all indices k between i and j (More
    formally min(i,j) < k < max(i,j)).

    Choose any index of the array to start jumping from. Return the maximum
    number of indices that can be visited.

    Notice that it is not possible to jump outside of the array at any time.
    '''
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        graph = [[] for _ in range(n)]
        for i in range(n):
            # jump left (until no longer monotonic decreasing)
            for j in range(i-1, max(i-d-1, -1), -1):
                if arr[j] < arr[i]:
                    graph[i].append(j)
                else:
                    break
            # jump right (until no longer monotonic decreasing)
            for j in range(i+1, min(i+d+1, n)):
                if arr[j] < arr[i]:
                    graph[i].append(j)
                else:
                    break
        @cache
        def dfs(index:int) -> int:
            answer = 1
            for i in graph[index]:
                answer = max(answer, 1 + dfs(i))
            return answer
        return max(dfs(i) for i in range(n))

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [6,4,14,6,8,13,9,7,10,6,12]
        j = 2
        o = 4
        self.assertEqual(s.maxJumps(i,j), o)

    def test_two(self):
        s = Solution()
        i = [3,3,3,3,3]
        j = 3
        o = 1
        self.assertEqual(s.maxJumps(i,j), o)

    def test_three(self):
        s = Solution()
        i = [7,6,5,4,3,2,1]
        j = 1
        o = 7
        self.assertEqual(s.maxJumps(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)