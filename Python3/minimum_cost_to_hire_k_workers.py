# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import heapq
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    There are n workers. Given two integer arrays quality and wage where
    quality[i] is the quality of the ith worker and wage[i] is the minimum wage
    expectation for the ith worker.

    Hire exactly k workers to a form a paid group. To hire a group of k workers,
    they must be paid according to the following rules:
    1) Every worker in the paid group must be paid at least their minimum wage
       expectation.
    2) In the group, each worker's pay must be directly proportional to their
       quality. This means if a worker's quality is double that of another
       worker in the group, then they must be paid twice as much as the other
       worker.
    
    Given the integer k, return the least amount of money needed to form a paid
    group satisfying the above conditions. Answers within 10^-5 of the actual
    answer will be accepted.
    '''
    # based on LeetCode Editorial
    # https://leetcode.com/problems/minimum-cost-to-hire-k-workers/?envType=daily-question&envId=2024-05-11
    # O(n log n + n log k) time O(n + k) space
    # consider workers in order of wage/quality ratio
    # keep in a queue the k lowest quality workers
    # update answer by calculating the current coset
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        answer = float('inf')
        proportional = sorted((w/q,w,q) for w,q in zip(wage,quality))
        q = []
        quality = 0
        for a,b,c in proportional:
            # add worker to group
            heapq.heappush(q,-c)
            # running total of quality
            quality += c
            # too many workers
            if len(q) > k:
                quality += heapq.heappop(q)
            # update answer
            if len(q) == k:
                answer = min(answer, quality * a)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [10,20,5]
        j = [70,50,30]
        k = 2
        o = 105.0
        self.assertEqual(s.mincostToHireWorkers(i,j,k), o)

    def test_two(self):
        s = Solution()
        i = [3,1,10,10,1]
        j = [4,8,2,2,7]
        k = 3
        o = 30.66667
        self.assertAlmostEqual(s.mincostToHireWorkers(i,j,k), o, 5)

if __name__ == '__main__':
    unittest.main(verbosity=2)