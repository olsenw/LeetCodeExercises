# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import heapq
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 0-indexed integer array costs where costs[i] is the cost of hiring
    the ith worker.

    Given two integers k and candidates. Hire exactly k workers according to the
    following rules:
    * There will be k hiring sessions where exactly one worker will be hired per
      session.
    * In each hiring session, choose the worker with the lowest cost from either
      the first candidates workers or the last candidates workers. Break the tie
      by the smallest index.
    * If there are fewer than candidates workers remaining, choose the worker
      with the lowest cost among them. Break the tie by the smallest index.
    * A worker can only be chosen once.

    Return the total cost to hire exactly k workers.
    '''
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        answer = 0
        h = []
        i,j = 0, len(costs) - 1
        for _ in range(candidates):
            if i <= j:
                heapq.heappush(h, (costs[i], i))
                i += 1
            if i <= j:
                heapq.heappush(h, (costs[j], j))
                j -= 1
        for _ in range(k):
            c, k = heapq.heappop(h)
            answer += c
            if i <= j:
                if k < i:
                    heapq.heappush(h, (costs[i], i))
                    i += 1
                else:
                    heapq.heappush(h, (costs[j], j))
                    j -= 1
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [17,12,10,2,7,2,11,20,8]
        j = 3
        k = 4
        o = 11
        self.assertEqual(s.totalCost(i,j,k), o)

    def test_two(self):
        s = Solution()
        i = [1,2,4,1]
        j = 3
        k = 3
        o = 4
        self.assertEqual(s.totalCost(i,j,k), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)