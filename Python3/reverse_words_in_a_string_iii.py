# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given a string s, reverse the order of characters in each word within a
    sentence while still preserving whitespace and initial word order.
    '''
    def reverseWords(self, s: str) -> str:
        return " ".join(i[::-1] for i in s.split())

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "Let's take LeetCode contest"
        o = "s'teL ekat edoCteeL tsetnoc"
        self.assertEqual(s.reverseWords(i), o)

    def test_two(self):
        s = Solution()
        i = "God Ding"
        o = "doG gniD"
        self.assertEqual(s.reverseWords(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)