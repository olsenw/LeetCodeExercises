# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an array of integers nums, half of the integers in nums are odd, and
    the other half are even.

    Sort the array so that whenever nums[i] is odd, 1 is odd, and whenever
    nums[i] is even, i is even.

    Return any answer array that satisfies this condition.
    '''
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even = [n for n in nums if n % 2 == 0]
        odds = [n for n in nums if n % 2 == 1]
        answer = []
        for i,j in zip(even, odds):
            answer.append(i)
            answer.append(j)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [4,2,5,7]
        o = [4,5,2,7]
        self.assertEqual(s.sortArrayByParityII(i), o)

    def test_two(self):
        s = Solution()
        i = [2,3]
        o = [2,3]
        self.assertEqual(s.sortArrayByParityII(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)