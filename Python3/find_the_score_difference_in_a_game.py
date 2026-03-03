# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums, where nums[i] represents the points scored in
    the ith game.

    There are exactly two players. Initially, the first player is active and the
    second player is inactive.

    The following rules apply sequentially for each game i:
    * If nums[i] is odd, the active and inactive players swap roles.
    * In every 6th game (that is, game indies 5,11,17,...) the active and
      inactive players swap roles.
    * The active player plays the ith game and gains nums[i] points.

    Return the score difference, defined as the first player's total score minus
    the second player's total score.
    '''
    def scoreDifference(self, nums: List[int]) -> int:
        a,b = 0,0
        active = True
        swap = 5
        for i in range(len(nums)):
            if nums[i] % 2:
                active = not active
            if i == swap:
                active = not active
                swap += 6
            if active:
                a += nums[i]
            else:
                b += nums[i]
        return a-b

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,3]
        o = 0
        self.assertEqual(s.scoreDifference(i), o)

    def test_two(self):
        s = Solution()
        i = [2,4,2,1,2,1]
        o = 4
        self.assertEqual(s.scoreDifference(i), o)

    def test_three(self):
        s = Solution()
        i = [1]
        o = -1
        self.assertEqual(s.scoreDifference(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)