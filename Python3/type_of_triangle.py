# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 0-indexed integer array nums of size 3 which can form the sides of a
    triangle.
    * A triangle is called equilateral if it has all sides of equal length.
    * A triangle is called isosceles if it has exactly two sides of equal
      length.
    * A triangle is called scalene if all edges are of different lengths.

    Return a string representing the type of triangle that can be formed or
    "none" if it cannot form a triangle.
    '''
    def triangleType(self, nums: List[int]) -> str:
        nums.sort()
        if nums[0] + nums[1] <= nums[2]:
            return "none"
        if nums[0] == nums[1] == nums[2]:
            return "equilateral"
        if nums[0] == nums[1] or nums[0] == nums[2] or nums[1] == nums[2]:
            return "isosceles"
        return "scalene"

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [3,3,3]
        o = "equilateral"
        self.assertEqual(s.triangleType(i), o)

    def test_two(self):
        s = Solution()
        i = [3,4,5]
        o = "scalene"
        self.assertEqual(s.triangleType(i), o)

    def test_three(self):
        s = Solution()
        i = [1,1,2]
        o = "none"
        self.assertEqual(s.triangleType(i), o)

    def test_three(self):
        s = Solution()
        i = [2,2,3]
        o = "isosceles"
        self.assertEqual(s.triangleType(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)