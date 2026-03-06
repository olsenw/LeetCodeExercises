# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an array bulbs of integers between 1 and 100.

    There are 100 light bulbs numbered from 1 to 100. All of them are switched
    off initially.

    For each element bulbs[i] in the array bulbs:
    * If the bulbs[i]th light bulb is currently off, switch it on.
    * Otherwise, switch it off.

    Return the list of integers denoting the light bulbs that are on in the end,
    sorted in ascending order. If no bulb is on, return an empty list.
    '''
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        lights = [False] * 100
        for bulb in bulbs:
            lights[bulb-1] = not lights[bulb-1]
        return [i+1 for i in range(100) if lights[i]]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [10,30,20,10]
        o = [20,30]
        self.assertEqual(s.toggleLightBulbs(i), o)

    def test_two(self):
        s = Solution()
        i = [100,100]
        o = []
        self.assertEqual(s.toggleLightBulbs(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)