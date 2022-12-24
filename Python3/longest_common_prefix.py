# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from itertools import zip_longest
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Write a function to find the longest common prefix string amongst an array
    of strings.

    If there is no common prefix, return an empty string "".
    '''
    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer = strs[0]
        for s in strs[1:]:
            i = 0
            for i,(j,k) in enumerate(zip_longest(answer, s)):
                if j != k:
                    break
            else:
                i += 1
            answer = answer[:i]
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = ["flower","flow","flight"]
        o = "fl"
        self.assertEqual(s.longestCommonPrefix(i), o)

    def test_two(self):
        s = Solution()
        i = ["dog","racecar","car"]
        o = ""
        self.assertEqual(s.longestCommonPrefix(i), o)

    def test_three(self):
        s = Solution()
        i = ["",""]
        o = ""
        self.assertEqual(s.longestCommonPrefix(i), o)

    def test_four(self):
        s = Solution()
        i = ["ab", "a"]
        o = "a"
        self.assertEqual(s.longestCommonPrefix(i), o)

    def test_five(self):
        s = Solution()
        i = ["flower","flower","flower","flower"]
        o = "flower"
        self.assertEqual(s.longestCommonPrefix(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)