# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a list of 24-hour clock time points in "HH:MM" format, return the
    minimum minutes difference between any two time points in the list.
    '''
    def findMinDifference(self, timePoints: List[str]) -> int:
        answer = 24 * 60
        timePoints = sorted(60 * int(tp[:2]) + int(tp[3:5]) for tp in timePoints)
        timePoints.append(timePoints[0] + answer)
        for i in range(len(timePoints) - 1):
            answer = min(answer, timePoints[i+1] - timePoints[i])
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = ["23:59","00:00"]
        o = 1
        self.assertEqual(s.findMinDifference(i), o)

    def test_two(self):
        s = Solution()
        i = ["00:00","23:59","00:00"]
        o = 0
        self.assertEqual(s.findMinDifference(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)