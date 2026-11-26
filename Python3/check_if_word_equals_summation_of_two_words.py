# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    The letter value of a letter is its position in the alphabet starting from 0
    (ie 'a' -> 0, 'b' -> 1, 'c' -> 2, etc.).

    The numerical value of some string of lowercase English letters s is the
    concatenation of the letter values of each letter in s, which is then
    converted into an integer.
    * For example, if s = "acb", concatenate each letter's letter value,
      resulting in "021". After converting it, it is 21.
    
    Given three strings firstWord, secondWord, and thirdWord, each consisting of
    lowercase English letters 'a' through 'j' inclusive.

    Return true if the summation of the numerical values of firstWord and
    secondWord equals the numerical value of targetWord, or false otherwise.
    '''
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        # v = {'a':'0', 'b':'1', 'c':'2', 'd':'3', 'e':'4', 'f':'5', 'g':'6', 'h':'7', 'i':'8', 'j':'9'}
        def value(word:str) -> int:
            # return int(''.join(str(ord(i) - ord('a')) for i in word))
            answer = 0
            for c in word:
                answer *= 10
                answer += ord(c) - ord('a')
            return answer
        return value(firstWord) + value(secondWord) == value(targetWord)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "acb"
        j = "cba"
        k = "cdb"
        o = True
        self.assertEqual(s.isSumEqual(i,j,k), o)

    def test_two(self):
        s = Solution()
        i = "aaa"
        j = "a"
        k = "aab"
        o = False
        self.assertEqual(s.isSumEqual(i,j,k), o)

    def test_three(self):
        s = Solution()
        i = "aaa"
        j = "a"
        k = "aaaa"
        o = True
        self.assertEqual(s.isSumEqual(i,j,k), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)