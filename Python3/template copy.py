# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums, return the number of subarrays filled with 0.

    A subarray is a contiguous non-empty sequence of elements within an array.
    '''
    # looked up how to calculate the number of subarrays for an array of length n
    # https://math.stackexchange.com/questions/1194584/the-total-number-of-subarrays
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        answer = 0
        current = 0
        for n in nums:
            if n == 0:
                current += 1
            else:
                answer += current * (current + 1) // 2
                current = 0
        return answer + current * (current + 1) // 2

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,3,0,0,2,0,0,4]
        o = 6
        self.assertEqual(s.zeroFilledSubarray(i), o)

    def test_two(self):
        s = Solution()
        i = [0,0,0,2,0,0]
        o = 9
        self.assertEqual(s.zeroFilledSubarray(i), o)

    def test_three(self):
        s = Solution()
        i = [2,10,2019]
        o = 0
        self.assertEqual(s.zeroFilledSubarray(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)