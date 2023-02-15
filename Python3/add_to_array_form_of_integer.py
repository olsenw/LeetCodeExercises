# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set

class Solution:
    '''
    The array-form of an integer is an array representing its digits in left to
    right order. (1321 -> [1,3,2,1])

    Given num, the array-form of an integer, and an integer k, return the
    array-form of the integer num + k
    '''
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        def toNum(array: List[int]) -> int:
            a = 0
            for i in array:
                a *= 10
                a += i
            return a
        def toArray(num: int) -> List[int]:
            a = []
            while num:
                a.append(num % 10)
                num //= 10
            return a[::-1]
        return toArray(toNum(num) + k)

    '''
    smarter way would be to take digit at a time from k and do logic to add to
    num array.
    '''

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,0,0]
        j = 34
        o = [1,2,3,4]
        self.assertEqual(s.addToArrayForm(i,j), o)

    def test_two(self):
        s = Solution()
        i = [2,7,4]
        j = 181
        o = [4,5,5]
        self.assertEqual(s.addToArrayForm(i,j), o)

    def test_three(self):
        s = Solution()
        i = [2,1,5]
        j = 806
        o = [1,0,2,1]
        self.assertEqual(s.addToArrayForm(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)