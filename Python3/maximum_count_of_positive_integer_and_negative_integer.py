# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    def maximumCount_lazy(self, nums: List[int]) -> int:
        return max(sum(i > 0 for i in nums), sum(i < 0 for i in nums))

    def maximumCount(self, nums: List[int]) -> int:
        a,b = 0,0
        for n in nums:
            if n > 0:
                a += 1
            elif n < 0:
                b += 1
        return max(a,b)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [-2,-1,-1,1,2,3]
        o = 3
        self.assertEqual(s.maximumCount(i), o)

    def test_two(self):
        s = Solution()
        i = [-3,-2,-1,0,0,1,2]
        o = 3
        self.assertEqual(s.maximumCount(i), o)

    def test_three(self):
        s = Solution()
        i = [5,20,66,1314]
        o = 4
        self.assertEqual(s.maximumCount(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)