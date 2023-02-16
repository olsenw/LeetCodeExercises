# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import deque
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set

class Solution:
    '''
    Given a 0-indexed integer array nums.

    The concatenation of two numbers is the number formed by concatenating their
    numerals (ie [15, 49] -> 1549).

    The concatenation value of nums is initially equal to 0. Perform this
    operation until nums becomes empty:
    * If there exists more than one number in nums, pick the first and last
      element in nums respectively and add the value of their concatenation to
      the concatenation value of nums, then delete the first and last element
      from nums.
    * If one element exists, add its value to he concatenation value of nums,
      then delete it.
    
    Return the concatenation value of nums.
    '''
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        a = 0
        d = deque(str(n) for n in nums)
        while len(d) > 1:
            a += int(d.popleft() + d.pop())
        if d:
            a += int(d.pop())
        return a

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [7,52,2,4]
        o = 596
        self.assertEqual(s.findTheArrayConcVal(i), o)

    def test_two(self):
        s = Solution()
        i = [5,14,13,8,12]
        o = 673
        self.assertEqual(s.findTheArrayConcVal(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)