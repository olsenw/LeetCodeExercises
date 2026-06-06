# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 0-indexed integer array nums of size n.

    Define two arrays leftSum and rightSum where:
    * leftSum[i] is the sum of elements to the left of the index i in the array
      nums. If there is no such element, leftSum[i] = 0.
    * rightSum[i] is the sum of elements to the right of the index i in the
      array nums. If there is no such element, rightSum[i] = 0.
    
    Return an integer array answer of size n where
    answer[i] = |leftSum[i] - rightSum[i]|.
    '''
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [0] * n
        r = 0
        for i in range(1,n):
            r += nums[i-1]
            answer[i] = r
        r = 0
        for i in range(n-2,-1,-1):
            r += nums[i+1]
            answer[i] = abs(answer[i] - r)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [10,4,8,3]
        o = [15,1,11,22]
        self.assertEqual(s.leftRightDifference(i), o)

    def test_two(self):
        s = Solution()
        i = [1]
        o = [0]
        self.assertEqual(s.leftRightDifference(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)