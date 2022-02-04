# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given a binary array nums, return the maximum length of a contiguous
    subarray with an equal number of 0 and 1.
    '''
    def findMaxLength_brute(self, nums: List[int]) -> int:
        m = 0
        for i in range(len(nums)):
            c = 0
            for j in range(i, len(nums)):
                if nums[j]:
                    c += 1
                else:
                    c -= 1
                if c == 0:
                    m = max(m, j - i + 1)
        return m

    def findMaxLength(self, nums: List[int]) -> int:
        # count, first index of this count 
        d = {0:0}
        c = 0
        m = 0
        # enumerate returns number(start+index) and each element 
        for i, n in enumerate(nums, 1):
            # update running count
            if n:
                c += 1
            else:
                c -= 1
            # check if this count has been seen before
            if c in d:
                # max is first seen to current index
                m = max(m, i - d[c])
            else:
                # first time seen this count
                d[c] = i
        return m

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [0,1]
        o = 2
        self.assertEqual(s.findMaxLength_brute(i), o)
        self.assertEqual(s.findMaxLength(i), o)

    def test_two(self):
        s = Solution()
        i = [0,1,0]
        o = 2
        self.assertEqual(s.findMaxLength_brute(i), o)
        self.assertEqual(s.findMaxLength(i), o)

    def test_three(self):
        s = Solution()
        i = [0,1,1,0]
        o = 4
        self.assertEqual(s.findMaxLength_brute(i), o)
        self.assertEqual(s.findMaxLength(i), o)

    def test_four(self):
        s = Solution()
        i = [0,1] * 50000
        o = 100000
        # self.assertEqual(s.findMaxLength_brute(i), o)
        self.assertEqual(s.findMaxLength(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)