# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a sorted array nums of n non-negative integers and an integer
    maximumBit. Perform the following query n times:
    1) Find a non-negative integer k < 2^maximumBit such that nums[0] XOR
       nums[1] XOR ... XOR nums[nums.length - 1] XOR k is maximized. k is the
       answer to the ith query.
    2) Remove the last element from the current array nums.

    Return an array answer, where answer[i] is the answer to the ith query.
    '''
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        answer = []
        k = (1 << maximumBit) - 1
        x = 0
        for n in nums:
            x ^= n
            answer.append(x ^ k)
        return answer[::-1]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [0,1,1,3], 2
        o = [0,3,2,3]
        self.assertEqual(s.getMaximumXor(*i), o)

    def test_two(self):
        s = Solution()
        i = [2,3,4,7], 3
        o = [5,2,6,5]
        self.assertEqual(s.getMaximumXor(*i), o)

    def test_three(self):
        s = Solution()
        i = [0,1,2,2,5,7], 3
        o = [4,3,6,4,6,7]
        self.assertEqual(s.getMaximumXor(*i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)