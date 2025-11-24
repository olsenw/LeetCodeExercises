# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a binary array nums (0-indexed).

    xi is defined as the number whose binary representation is the subarray
    nums[o..i] (from most-significant-bit to least-significant-bit).

    Return an array of booleans answer where answer [i] is true if xi is
    divisible by 5.
    '''
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        answer = []
        running = 0
        for n in nums:
            running <<= 1
            running += n
            answer.append(running % 5 == 0)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [0,1,1]
        o = [True, False, False]
        self.assertEqual(s.prefixesDivBy5(i), o)

    def test_two(self):
        s = Solution()
        i = [1,1,1]
        o = [False, False, False]
        self.assertEqual(s.prefixesDivBy5(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)