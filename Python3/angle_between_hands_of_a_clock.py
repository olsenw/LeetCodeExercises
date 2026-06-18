# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given two numbers, hour and minutes, return the smaller angle (in degrees)
    formed between the hour and the minute hand.

    Answers within 10^-5 of the actual answer will be accepted as correct.
    '''
    # does not account for partial position of hour hand (ie between hour marks)
    def angleClock_fails(self, hour: int, minutes: int) -> float:
        hour = ((360 // 12) * hour) % 360
        minutes = ((360 // 60) * minutes) % 360
        angle = max(hour, minutes) - min(hour, minutes)
        return 1.0 * min(angle, 360 - angle)

    def angleClock(self, hour: int, minutes: int) -> float:
        h = 360 // 12
        m = 360 // 60
        hour = (h * hour) % 360 + (h * (minutes / 60.0))
        minutes = (m * minutes) % 360
        angle = max(hour, minutes) - min(hour, minutes)
        return min(angle, 360-angle)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 12
        j = 30
        o = 165.0
        self.assertAlmostEqual(s.angleClock(i,j), o, 5)

    def test_two(self):
        s = Solution()
        i = 3
        j = 30
        o = 75.0
        self.assertAlmostEqual(s.angleClock(i,j), o, 5)

    def test_three(self):
        s = Solution()
        i = 3
        j = 15
        o = 7.5
        self.assertAlmostEqual(s.angleClock(i,j), o, 5)

if __name__ == '__main__':
    unittest.main(verbosity=2)