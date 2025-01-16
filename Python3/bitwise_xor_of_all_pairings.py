# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given two 0-indexed arrays, nums1 and nums2, consisting of non-negative
    integers. There exists another array, nums3, which contains the bitwise XOR
    of all parings of integers between nums1 and nums2 (every integer in nums1
    is paired with every integer in nums2 exactly once).

    Return the bitwise XOR of all integers in nums3.
    '''
    # hints are very helpful
    # a xor a = 0 | a xor b xor a = a xor a xor b = b
    # ie only xor an array if the number would have an odd number of pairings
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        m,n = len(nums1), len(nums2)
        answer = 0
        if n % 2:
            for x in nums1:
                answer ^= x
        if m % 2:
            for x in nums2:
                answer ^= x
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [2,1,3]
        j = [10,2,5,0]
        o = 13
        self.assertEqual(s.xorAllNums(i,j), o)

    def test_two(self):
        s = Solution()
        i = [1,2]
        j = [3,4]
        o = 0
        self.assertEqual(s.xorAllNums(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)