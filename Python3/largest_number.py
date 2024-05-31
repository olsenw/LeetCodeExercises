# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import defaultdict, deque
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a list of non-negative integers nums, arrange them such that they form
    the largest number and return it.

    Since the result may be very large, return a string instead of an integer.
    '''
    # passes 188 / 232 see test case three
    def largestNumber_wrong(self, nums: List[int]) -> str:
        a = [str(n) for n in nums]
        a = sorted(a, key=lambda x: x.ljust(10, '0'), reverse=True)
        a = ''.join(a)
        return a

    def largestNumber_fails(self, nums: List[int]) -> str:
        a = sorted(nums, key=lambda x: (str(x).ljust(10,':'), -x), reverse=True)
        return ''.join(str(n) for n in a)

    # based on editorial by LeetCode
    # https://leetcode.com/problems/largest-number/editorial/
    def largestNumber(self, nums: List[int]) -> str:
        # need class to pass custom less than to the lamda
        class Comparator(str):
            # redefine less than
            # concatenate two strings and see which concatenation is larger
            def __lt__(self, value: str) -> bool:
                return self+value > value+self
        nums = ''.join(sorted((str(n) for n in nums), key=Comparator))
        return '0' if nums[0] == '0' else nums

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [10,2]
        o = "210"
        self.assertEqual(s.largestNumber(i), o)

    def test_two(self):
        s = Solution()
        i = [3,30,34,5,9]
        o = "9534330"
        self.assertEqual(s.largestNumber(i), o)

    def test_three(self):
        s = Solution()
        i = [111311, 1113]
        o = "1113111311"
        self.assertEqual(s.largestNumber(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)