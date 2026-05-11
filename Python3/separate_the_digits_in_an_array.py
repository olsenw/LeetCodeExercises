# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an array of positive integers nums, return an array answer that
    consists of the digits of each integer in nums after separating them in the
    same order they appear in nums.

    To separate the digits of an integer is to get all digits it has in the same
    order.
    '''
    def separateDigits(self, nums: List[int]) -> List[int]:
        answer = []
        for n in nums:
            a = []
            while n > 0:
                a.append(n % 10)
                n //= 10
            answer.extend(a[::-1])
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [13,25,83,77]
        o = [1,3,2,5,8,3,7,7]
        self.assertEqual(s.separateDigits(i), o)

    def test_two(self):
        s = Solution()
        i = [7,1,3,9]
        o = [7,1,3,9]
        self.assertEqual(s.separateDigits(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)