# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 1-indexed integer array nums of length n.

    An element nums[i] of nums is called special if i divides n, ie n % i == 0.

    Return the sum of the squares of all special elements of nums.
    '''
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        answer = 0
        for i in range(n):
            if n % (i + 1) == 0:
                answer += nums[i] * nums[i]
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,3,4]
        o = 21
        self.assertEqual(s.sumOfSquares(i), o)

    def test_two(self):
        s = Solution()
        i = [2,7,1,19,18,3]
        o = 63
        self.assertEqual(s.sumOfSquares(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)