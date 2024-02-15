# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an array of positive integers nums of length n.

    A polygon is a closed plane figure that has at least 3 sides. The longest
    side of a polygon is smaller than the sum of its other sides.

    Conversely, if there are k (k >= 3) positive real numbers a1, a2, a3, ...,
    ak, where a1 <= a2 <= a3 <= ... <= ak and a1 + a2 + a3 + ... + ak-1 > ak,
    then there always exists a polygon with k sides whose lengths are a1, a2,
    a3, ... ak.

    The perimeter of a polygon is the sum of lengths of its sides.

    Return the largest possible perimeter of a polygon whose sides can be formed
    from nums, or -1 if it is not possible to create a polygon.
    '''
    def largestPerimeter_fails(self, nums: List[int]) -> int:
        nums.sort()
        if nums[0] + nums[1] <= nums[2]:
            return -1
        p = nums[0] + nums[1] + nums[2]
        for n in nums[3:]:
            if n >= p:
                break
            p += n
        return p

    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        a = -1
        p = nums[0] + nums[1]
        for n in nums[2:]:
            if p > n:
                a = p + n
            p += n
        return a

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [5,5,5]
        o = 15
        self.assertEqual(s.largestPerimeter(i), o)

    def test_two(self):
        s = Solution()
        i = [1,12,1,2,5,50,3]
        o = 12
        self.assertEqual(s.largestPerimeter(i), o)

    def test_three(self):
        s = Solution()
        i = [5,5,50]
        o = -1
        self.assertEqual(s.largestPerimeter(i), o)

    def test_four(self):
        s = Solution()
        i = [1,2,1]
        o = -1
        self.assertEqual(s.largestPerimeter(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)