# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

from collections import Counter

class Solution:
    '''
    Given an integer array nums and an integer k.

    In one operation two numbers may be removed from the array if the
    sum of the two numbers is equal to k.

    Return the maximum number of removals that can be performed on the
    array.
    '''
    def maxOperations(self, nums: List[int], k: int) -> int:
        c = Counter(nums)
        a = 0
        for i in c:
            a += min(c[i], c[k - i])
        return a // 2

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,3,4]
        j = 5
        o = 2
        self.assertEqual(s.maxOperations(i,j), o)

    def test_two(self):
        s = Solution()
        i = [3,1,3,4,3]
        j = 6
        o = 1
        self.assertEqual(s.maxOperations(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)