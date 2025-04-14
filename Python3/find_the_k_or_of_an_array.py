# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums, and an integer k. Let's introduce K-or
    operation by extending the standard bitwise OR. In k-or, a bit position in
    the result is set to 1 if at least k numbers in nums have a 1 in that
    position.

    Return the K-or of nums.
    '''
    def findKOr(self, nums: List[int], k: int) -> int:
        bits = [0] * 32
        for n in nums:
            i = 0
            while n:
                bits[i] += n & 1
                n >>= 1
                i += 1
        answer = 0
        for i in range(31,-1,-1):
            answer <<= 1
            answer |= bits[i] >= k
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [7,12,9,8,9,15]
        j = 4
        o = 9
        self.assertEqual(s.findKOr(i,j), o)

    def test_two(self):
        s = Solution()
        i = [2,12,1,11,4,5]
        j = 6
        o = 0
        self.assertEqual(s.findKOr(i,j), o)

    def test_three(self):
        s = Solution()
        i = [10,8,5,9,11,6,8]
        j = 1
        o = 15
        self.assertEqual(s.findKOr(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)