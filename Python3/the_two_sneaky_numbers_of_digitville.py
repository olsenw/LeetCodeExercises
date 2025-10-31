# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    In the town of Digitville, there was a list of numbers called nums
    containing integers from 0 to n - 1. Each number was supposed to appear
    exactly once in the list, however, two mischievous numbers sneaked in an
    additional time, making the list longer than usual.

    As the town detective, find these two sneaky numbers. Return an array of
    size two containing the two numbers (in any order), so peace can return to
    Digitville.
    '''
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        s = set()
        answer = []
        for n in nums:
            if n in s:
                answer.append(n)
            else:
                s.add(n)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [0,1,1,0]
        o = [1,0]
        self.assertEqual(s.getSneakyNumbers(i), o)

    def test_two(self):
        s = Solution()
        i = [0,3,2,1,3,2]
        o = [3,2]
        self.assertEqual(s.getSneakyNumbers(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)