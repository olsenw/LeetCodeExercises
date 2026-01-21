# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an array nums consisting of n prime integers.

    Construct an array ans of length n, such that, for each index i, the bitwise
    OR of ans[i] and ans[i]+1 is equal to nums[i],
    ie ans[i] OR ans[i+1] == nums[i].

    Additionally, minimize each value of ans[i] in the resulting array.

    If it is not possible to find such a value for ans[i] that satisfies the
    condition, then set ans[i] = -1.
    '''
    # based on hints
    # looked at patterns of bits in answer
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        answer = []
        for n in nums:
            if n % 2 == 0:
                answer.append(-1)
            else:
                i = 1
                while i & n > 0:
                    i <<= 1
                i >>= 1
                answer.append(n^i)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [2,3,5,7]
        o = [-1,1,4,3]
        self.assertEqual(s.minBitwiseArray(i), o)

    def test_two(self):
        s = Solution()
        i = [11,13,31]
        o = [9,12,15]
        self.assertEqual(s.minBitwiseArray(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)