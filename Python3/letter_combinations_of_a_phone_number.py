# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given a string containing digits from 2-9 inclusive, return all
    possible letter combinations that the number could represent. Return
    the answer in any order.

    A mapping of digit to letters (just like on the telephone buttons)
    is given below. Note that 1 does not map to any letters.
    2 -> abc
    3 -> def
    4 -> ghi
    5 -> jkl
    6 -> mno
    7 -> pqrs
    8 -> tuv
    9 -> wxyz
    '''
    mapping = {
        '2':['a','b','c'],
        '3':['d','e','f'],
        '4':['g','h','i'],
        '5':['j','k','l'],
        '6':['m','n','o'],
        '7':['p','q','r','s'],
        '8':['t','u','v'],
        '9':['w','x','y','z'],
        }
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        elif len(digits) == 1:
            return self.mapping[digits[0]]
        else:
            a = []
            lc = self.letterCombinations(digits[1:])
            for i in self.mapping[digits[0]]:
                for j in lc:
                    a.append(i + j)
            return a
    def letterCombinations_alt(self, digits: str) -> List[str]:
        if len(digits) > 1:
            a = []
            for i in self.letterCombinations(digits[1:]):
                for j in self.mapping[digits[0]]:
                    a.append(j + i)
            return a
        elif len(digits) == 1:
            return self.mapping[digits[0]]
        else:
            return []

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "23"
        o = ["ad","ae","af","bd","be","bf","cd","ce","cf"]
        self.assertEqual(s.letterCombinations(i), o)

    def test_two(self):
        s = Solution()
        i = ""
        o = []
        self.assertEqual(s.letterCombinations(i), o)

    def test_three(self):
        s = Solution()
        i = "2"
        o = ["a","b","c"]
        self.assertEqual(s.letterCombinations(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)