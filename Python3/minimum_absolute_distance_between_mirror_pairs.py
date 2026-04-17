# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums.

    A mirror pair is a pair of indices (i, j) such that:
    * 0 <= i < j < nums.length, and
    * reverse(nums[i]) == nums[j], where reverse(x) denotes the integer formed
      by reversing the digits of x. Leading zeros are omitted after reversing,
      for example reverse(120) = 21.
    
    Return the minimum absolute distance between the indices of any mirror pair.
    The absolute distance between indices i and j is abs(i - j).

    If no mirror pair exists, return -1.
    '''
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        n = len(nums)
        d = dict()
        answer = n
        for i,j in enumerate(nums):
            if j in d:
                answer = min(answer, i - d[j])
            r = int(str(j)[::-1])
            d[r] = i
        return answer if answer < n else -1

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [12,21,45,33,54]
        o = 1
        self.assertEqual(s.minMirrorPairDistance(i), o)

    def test_two(self):
        s = Solution()
        i = [120,21]
        o = 1
        self.assertEqual(s.minMirrorPairDistance(i), o)

    def test_three(self):
        s = Solution()
        i = [21,120]
        o = -1
        self.assertEqual(s.minMirrorPairDistance(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)