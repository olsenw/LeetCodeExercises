# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    The next greater element of some element x in an array is the first greater
    element that is to the right of x in the same array.

    Given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is
    a subset of nums2.

    For each 0 <= i < nums1.length, find the index j such that
    nums1[i] == nums2[j] and determine the next greater element of nums2[j] in
    nums2. If there is no next greater element, then the answer to this query is
    -1.

    Return an array ans of length nums1.length such that ans[i] is the next
    greater element as described above.
    '''
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = {n:-1 for n in nums1}
        mono = []
        for n in nums2[::-1]:
            while mono and mono[-1] <= n:
                mono.pop()
            if n in nums1 and mono:
                nums1[n] = mono[-1]
            mono.append(n)
        return [nums1[i] for i in nums1]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [4,1,2]
        j = [1,3,4,2]
        o = [-1,3,-1]
        self.assertEqual(s.nextGreaterElement(i,j), o)

    def test_two(self):
        s = Solution()
        i = [2,4]
        j = [1,2,3,4]
        o = [3,-1]
        self.assertEqual(s.nextGreaterElement(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)