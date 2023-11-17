# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    The pair sum of a pair (a,b) is equal to a + b. The maximum pair sum is the
    largest pair sum in a list of pairs.

    Given an array nums of even length n, pair up the elements of nums into
    n / 2 pairs such that:
    * Each element of nums is in exactly one pair and
    * The maximum pair sum is minimized.

    Returns the minimized maximum pair sum after optimally pairing up the
    elements.
    '''
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return max(nums[i] + nums[-i-1] for i in range(len(nums) // 2))

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [3,5,2,3]
        o = 7
        self.assertEqual(s.minPairSum(i), o)

    def test_two(self):
        s = Solution()
        i = [3,5,4,2,4,6]
        o = 8
        self.assertEqual(s.minPairSum(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)