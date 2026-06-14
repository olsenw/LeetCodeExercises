# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer timer representing the remaining time (in seconds) on a
    traffic signal.

    The signal follows these rules:
    * If timer == 0, the signal is "Green"
    * If timer == 30, the signal is "Orange"
    * If 30 < timer <= 90, the signal is "Red"

    Return the current state of the signal. If none of the above conditions are
    met, return "Invalid".
    '''
    def trafficSignal(self, timer: int) -> str:
        if timer == 0:
            return "Green"
        elif timer == 30:
            return "Orange"
        elif 30 < timer <= 90:
            return "Red"
        else:
            return "Invalid"

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 60
        o = "Red"
        self.assertEqual(s.trafficSignal(i), o)

    def test_two(self):
        s = Solution()
        i = 5
        o = "Invalid"
        self.assertEqual(s.trafficSignal(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)