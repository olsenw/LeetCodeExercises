# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given an array nums containing n distinct numbers int the range
    [0,n], return the only number in the range that is missing from the
    array.
    '''
    # O(n) time O(1) space
    def missingNumber_const(self, nums: List[int]) -> int:
        n = len(nums)
        s = (n * (n + 1)) // 2
        for n in nums:
            s -= n
        return s

    def missingNumber_const_faster(self, nums: List[int]) -> int:
        n = len(nums)
        return (n * (n + 1)) // 2 - sum(nums)

    # O(n) time O(n) space
    def missingNumber_set(self, nums: List[int]) -> int:
        s = [0] * (len(nums) + 1)
        for n in nums:
            s[n] = 1
        i = 0
        while s[i]:
            i += 1
        return i

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [3,0,1]
        o = 2
        self.assertEqual(s.missingNumber(i), o)

    def test_two(self):
        s = Solution()
        i = [0,1]
        o = 2
        self.assertEqual(s.missingNumber(i), o)

    def test_two(self):
        s = Solution()
        i = [9,6,4,2,3,5,7,0,1]
        o = 8
        self.assertEqual(s.missingNumber(i), o)

    def test_four(self):
        s = Solution()
        i = [2,1]
        o = 0
        self.assertEqual(s.missingNumber(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)