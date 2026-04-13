# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums (0-indexed) and two integers target and start,
    find an index i such that nums[i] == target and abs(i - start) is minimized.
    Note that abs(x) is the absolute value of x.

    Return abs(i - start).

    It is guaranteed that target exists in nums.
    '''
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        n = len(nums)
        answer = float('inf')
        for i in range(start,n):
            if nums[i] == target:
                answer = min(answer, abs(i - start))
                break
        for i in range(start,-1,-1):
            if nums[i] == target:
                answer = min(answer, abs(i - start))
                break
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,3,4,5]
        j = 3
        k = 3
        o = 1
        self.assertEqual(s.getMinDistance(i,j,k), o)

    def test_two(self):
        s = Solution()
        i = [1]
        j = 1
        k = 0
        o = 0
        self.assertEqual(s.getMinDistance(i,j,k), o)

    def test_three(self):
        s = Solution()
        i = [1,1,1,1,1,1,1,1,1,1]
        j = 1
        k = 0
        o = 0
        self.assertEqual(s.getMinDistance(i,j,k), o)

    def test_four(self):
        s = Solution()
        i = [5,3,6]
        j = 5
        k = 2
        o = 2
        self.assertEqual(s.getMinDistance(i,j,k), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)