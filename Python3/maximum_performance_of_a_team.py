# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

import heapq

class Solution:
    '''
    Given two integers n and k and two integer arrays speed and
    efficiency both of length n. There are n engineers numbered from 1
    to n. speed[i] and efficiency[i] represent the speed and efficiency
    of the ith engineer respectively.

    Choose at most k different engineers out of the n engineers to form
    a team with the maximum performance.

    The performance of a team is the sum of their engineer's speeds
    multiplied by the minimum efficiency among their engineers.

    Return the maximum performance of this team. Since the answer can be
    a huge number, return it modulo 10^9 + 7.
    '''
    # cases 54/55 time limit exceeded
    # O(n^2 log n) time
    def maxPerformance_tle(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        answer = 0
        engineers = sorted([z for z in zip(speed, efficiency)], key=lambda x:(-x[1],x[0]))
        for i in range(n):
            heap = []
            for j in range(i):
                if len(heap) < k - 1:
                    heapq.heappush(heap, engineers[j][0])
                else:
                    heapq.heappushpop(heap, engineers[j][0])
            answer = max(answer, (sum(heap) + engineers[i][0]) * engineers[i][1])
        return answer % (10**9 + 7)

    # O(n log n) time
    # got rid of unneeded for loop
    def maxPerformance_greedy(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        answer = 0
        engineers = sorted([z for z in zip(speed, efficiency)], key=lambda x:(-x[1],x[0]))
        runSum = 0
        heap = []
        for i in range(n):
            runSum += engineers[i][0]
            if len(heap) < k:
                heapq.heappush(heap, engineers[i][0])
            else:
                runSum -= heapq.heappushpop(heap, engineers[i][0])
            answer = max(answer, runSum * engineers[i][1])
        return answer % (10**9 + 7)

    # O(n log n) time
    def maxPerformance_greedy_alt(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        modulo = 10**9 + 7
        answer = 0
        # sorted by efficiency from high to low
        engineers = sorted(range(n), key=lambda x: -efficiency[x])
        runSum = 0
        heap = []
        for e in engineers:
            runSum += speed[e]
            if len(heap) < k:
                heapq.heappush(heap, speed[e])
            else:
                runSum -= heapq.heappushpop(heap, speed[e])
            answer = max(answer, runSum * efficiency[e])
        return answer % modulo

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [
            6,
            [2,10,3,1,5,8],
            [5,4,3,9,7,2],
            2
        ]
        o = 60
        self.assertEqual(s.maxPerformance(*i), o)

    def test_two(self):
        s = Solution()
        i = [
            6,
            [2,10,3,1,5,8],
            [5,4,3,9,7,2],
            3
        ]
        o = 68
        self.assertEqual(s.maxPerformance(*i), o)

    def test_three(self):
        s = Solution()
        i = [
            6,
            [2,10,3,1,5,8],
            [5,4,3,9,7,2],
            4
        ]
        o = 72
        self.assertEqual(s.maxPerformance(*i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)