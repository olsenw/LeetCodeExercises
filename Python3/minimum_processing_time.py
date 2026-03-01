# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a certain number of processors, each having 4 cores. The number of
    tasks to be executed is four times the number of processors. Each task must
    be assigned to a unique core, and each core can only by used once.

    Given an array processorTime representing the time each processor becomes
    available and an array tasks representing how long each task takes to
    complete. Return the minimum time needed to complete all tasks.
    '''
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        answer = 0
        processorTime.sort()
        tasks.sort(reverse=True)
        for i,j in enumerate(processorTime):
            answer = max(answer, j + max(tasks[4*i:4*i+5]))
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [8,10]
        j = [2,2,3,1,8,7,4,5]
        o = 16
        self.assertEqual(s.minProcessingTime(i,j), o)

    def test_two(self):
        s = Solution()
        i = [10,20]
        j = [2,3,1,2,5,8,4,3]
        o = 23
        self.assertEqual(s.minProcessingTime(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)