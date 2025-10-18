# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums and an integer k.

    It is possible to perform the following operation on each element of the
    array at most once:
    * Add an integer in the range [-k,k] to the element.

    Return the maximum possible number of distinct elements in nums after
    performing the operations.
    '''
    # brute force
    def maxDistinctElements_tle(self, nums: List[int], k: int) -> int:
        nums.sort()
        s = set()
        for n in nums:
            for i in range(n - k, n + k + 1):
                if i not in s:
                    s.add(i)
                    break
        return len(s)

    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        s = set()
        last = nums[0] - k - 1
        for n in nums:
            for i in range(max(last + 1, n - k), n + k + 1):
                if i not in s:
                    s.add(i)
                    last = i
                    break
        return len(s)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,2,3,3,4]
        j = 2
        o = 6
        self.assertEqual(s.maxDistinctElements(i,j), o)

    def test_two(self):
        s = Solution()
        i = [4,4,4,4]
        j = 1
        o = 3
        self.assertEqual(s.maxDistinctElements(i,j), o)

    def test_three(self):
        s = Solution()
        i = [56,56,54,54]
        j = 0
        o = 2
        self.assertEqual(s.maxDistinctElements(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)