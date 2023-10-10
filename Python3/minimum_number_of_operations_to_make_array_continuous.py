# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import bisect
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums. In one operation, it is possible to replace any
    element in nums with any integer.

    nums is considered continuous if both of the following conditions are
    fulfilled:
    * All elements in nums are unique.
    * The difference between the maximum element and the minimum element in nums
      equals nums.length - 1.
    
    Return the minimum number of operations to make nums continuous.
    '''
    def minOperations(self, nums: List[int]) -> int:
        k = len(nums) - 1
        nums = sorted(set(nums))
        answer = k + 1
        for i,x in enumerate(nums):
            j = bisect.bisect(nums, x + k)
            answer = min(answer, i + len(nums) - j)
        return answer + k - len(nums) + 1

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [4,2,5,3]
        o = 0
        self.assertEqual(s.minOperations(i), o)

    def test_two(self):
        s = Solution()
        i = [1,2,3,5,6]
        o = 1
        self.assertEqual(s.minOperations(i), o)

    def test_three(self):
        s = Solution()
        i = [1,10,100,1000]
        o = 3
        self.assertEqual(s.minOperations(i), o)

    def test_four(self):
        s = Solution()
        i = [1,1,1,1,2,3,4]
        o = 3
        self.assertEqual(s.minOperations(i), o)

    def test_five(self):
        s = Solution()
        i = [91, 8, 98, 16, 40, 66, 76, 41, 46, 59]
        o = 7
        self.assertEqual(s.minOperations(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)