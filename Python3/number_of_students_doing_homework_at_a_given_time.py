# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given two integer arrays startTime and endTime and given an integer
    queryTime.

    The ith student started doing their homework at the time startTime[i] and
    finished it at time endTime[i].

    Return the number of students doing their homework at time queryTime. More
    formally, return the number of students where queryTime lays in the interval
    [startTime[i, endTime[i]]] inclusive.
    '''
    def busyStudent(self, startTime: list[int], endTime: list[int], queryTime: int) -> int:
        answer = 0
        for i,j in zip(startTime, endTime):
            answer += i <= queryTime <= j
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,3]
        j = [3,2,7]
        k = 4
        o = 1
        self.assertEqual(s.busyStudent(i,j,k), o)

    def test_two(self):
        s = Solution()
        i = [4]
        j = [4]
        k = 4
        o = 1
        self.assertEqual(s.busyStudent(i,j,k), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)