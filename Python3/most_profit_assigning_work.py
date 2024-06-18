# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import bisect
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    There are n jobs and m workers. Given three arrays: difficulty, profit, and
    worker where:
    * difficulty[i] and profit[i] are the difficulty and the profit of the ith
      job, and
    * worker[j] is the ability of the jth worker (ie the jth worker can only
      complete a job with difficulty at most worker[j]).
    
    Every worker can be assigned at most one job, but one job can be completed
    multiple times.

    Return the maximum profit that be achieved after assigning the workers to
    the jobs.
    '''
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        answer = 0
        worker.sort()
        s = sorted((i,j) for i,j in zip(difficulty, profit))
        m = 0
        i = 0
        for w in worker:
            while i < len(s) and s[i][0] <= w:
                m = max(m, s[i][1])
                i += 1
            answer += m
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [2,4,6,8,10]
        j = [10,20,30,40,50]
        k = [4,5,6,7]
        o = 100
        self.assertEqual(s.maxProfitAssignment(i,j,k), o)

    def test_two(self):
        s = Solution()
        i = [85,47,57]
        j = [24,66,99]
        k = [40,25,25]
        o = 0
        self.assertEqual(s.maxProfitAssignment(i,j,k), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)