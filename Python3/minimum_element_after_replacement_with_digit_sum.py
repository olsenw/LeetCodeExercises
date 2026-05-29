# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums.

    Every element in nums is replaced with the sum of its digits.

    Return the minimum element in nums after all replacements.
    '''
    def minElement(self, nums: List[int]) -> int:
        def element(i:int) -> int:
            answer = 0
            while i:
                answer += i % 10
                i //= 10
            return answer
        return min(element(i) for i in nums)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [10,12,13,14]
        o = 1
        self.assertEqual(s.minElement(i), o)

    def test_two(self):
        s = Solution()
        i = [1,2,3,4]
        o = 1
        self.assertEqual(s.minElement(i), o)

    def test_two(self):
        s = Solution()
        i = [999,19,199]
        o = 10
        self.assertEqual(s.minElement(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)