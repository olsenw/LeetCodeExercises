# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import heapq
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Suppose LeetCode will start is IPO soon. In order to sell a good price of
    its shares to Venture Capital, LeetCode would like to work on some projects
    to increase its capital before the IPO. Since it has limited resources, it
    can only finish at most k distinct projects before the IPO. Help LeetCode
    design the best way to maximize its total capital after finishing at most k
    distinct projects.

    Given n projects where the ith project has a pure profit profits[i] and a
    minimum capital of capital[i] is needed to start it.

    Initially, there is w capital. When a project is finished, the pure profit
    is added to the total capital.

    Pick a list of at most k distinct projects from given projects to maximize
    the final capital, and return the final maximized capital.

    The test cases are designed to fit in a 32-bit signed integer.
    '''
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        pairs = sorted(i for i in zip(capital,profits))
        index = 0
        heap = []
        while k > 0:
            while index < len(pairs) and pairs[index][0] <= w:
                heapq.heappush(heap, -pairs[index][1])
                index += 1
            if not heap:
                break
            w += -heapq.heappop(heap)
            k -= 1
        return w

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 2
        j = 0
        k = [1,2,3]
        l = [0,1,1]
        o = 4
        self.assertEqual(s.findMaximizedCapital(i,j,k,l), o)

    def test_two(self):
        s = Solution()
        i = 3
        j = 0
        k = [1,2,3]
        l = [0,1,2]
        o = 6
        self.assertEqual(s.findMaximizedCapital(i,j,k,l), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)