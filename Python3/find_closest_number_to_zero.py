# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums of size n, return the number with the value
    closest to 0 in nums. If there are multiple answers, return the number with
    the largest value.
    '''
    def findClosestNumber(self, nums: List[int]) -> int:
        answer = 10**9 + 7
        diff = 10**9 + 7
        for n in nums:
            a = abs(n)
            if a < diff or (a == diff and n > answer):
                diff = a
                answer = n
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [-4,-2,1,4,8]
        o = 1
        self.assertEqual(s.findClosestNumber(i), o)

    def test_two(self):
        s = Solution()
        i = [2,-1,1]
        o = 1
        self.assertEqual(s.findClosestNumber(i), o)

    def test_three(self):
        s = Solution()
        i = [2,0,-1,1]
        o = 0
        self.assertEqual(s.findClosestNumber(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)