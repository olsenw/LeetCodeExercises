# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given an array of positive integers nums. It is possible to erase a
    subarray containing unique elements. The score of the erased
    subarray is equal to the sum of its elements.

    Return the maximum score that can be obtained by erasing exactly one
    subarray.

    An array b is a subarray of a if it forms a contiguous subsequence
    of a, that is, if it is equal to a[l],a[l+1],...,a[r] for some (l,r)
    '''
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        h = {}
        l = a = s = 0
        for r in range(len(nums)):
            a += nums[r]
            if nums[r] in h:
                while l < h[nums[r]]:
                    a -= nums[l]
                    l += 1
            h[nums[r]] = r + 1
            s = max(s, a)
        return s

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [4,2,4,5,6]
        o = 17
        self.assertEqual(s.maximumUniqueSubarray(i), o)

    def test_two(self):
        s = Solution()
        i = [5,2,1,2,5,2,1,2,5]
        o = 8
        self.assertEqual(s.maximumUniqueSubarray(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)