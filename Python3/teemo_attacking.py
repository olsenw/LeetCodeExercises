# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Our hero Teemo is attacking an enemy Ashe with poison attacks! When Teemo
    attacks Ashe, Ashe gets poisoned for exactly duration seconds. More
    formally, an attack at second t will mean Ashe is poisoned during the
    inclusive time interval [t, t + duration - 1]. If Teemo attacks again before
    the poison effect ends, the timer for it is reset, and the poison effect
    will end durations seconds after the new attack.

    Given a non-decreasing integer array timeSeries, where timeSeries[i] denotes
    that Teemo attacks Ashe at second timeSeries[i], and an integer duration.

    Return the total number of seconds that Ashe is poisoned.
    '''
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        answer = 0
        start = timeSeries[0]
        end = timeSeries[0] + duration
        for t in timeSeries[1:]:
            if end < t:
                answer += end - start
                start = t
            end = t + duration
        return answer + end - start

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,4]
        j = 2
        o = 4
        self.assertEqual(s.findPoisonedDuration(i,j), o)

    def test_two(self):
        s = Solution()
        i = [1,2]
        j = 2
        o = 3
        self.assertEqual(s.findPoisonedDuration(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)