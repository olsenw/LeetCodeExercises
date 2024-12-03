# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 0-indexed string s and a 0-indexed integer array spaces that
    describes the indices in the original string where spaces will be added.
    Each space should be inserted before the character at the given index.

    Return the modified string after the spaces have been added.
    '''
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        answer = ""
        spaces.append(len(s))
        j = 0
        for i in range(len(s)):
            if i == spaces[j]:
                answer += " "
                j += 1
            answer += s[i]
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "LeetcodeHelpsMeLearn"
        j = [8,13,15]
        o = "Leetcode Helps Me Learn"
        self.assertEqual(s.addSpaces(i,j), o)

    def test_two(self):
        s = Solution()
        i = "icodeinpython"
        j = [1,5,7,9]
        o = "i code in py thon"
        self.assertEqual(s.addSpaces(i,j), o)

    def test_three(self):
        s = Solution()
        i = "spacing"
        j = [0,1,2,3,4,5,6]
        o = " s p a c i n g"
        self.assertEqual(s.addSpaces(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)