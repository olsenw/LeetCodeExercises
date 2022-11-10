# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given a string s consisting of lowercase English letters. A duplicate
    removal consists of choosing two adjacent and equal letters and removing
    them.

    Repeatedly make duplicate removals on s until it is no longer possible.

    Return the final string after all such duplicate removals have been made. It
    can be proven that the answer is unique.
    '''
    def removeDuplicates(self, s: str) -> str:
        answer = []
        for c in s:
            if answer and c == answer[-1]:
                answer.pop()
            else:
                answer.append(c)
        return ''.join(answer)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "abbaca"
        o = "ca"
        self.assertEqual(s.removeDuplicates(i), o)

    def test_two(self):
        s = Solution()
        i = "azxxzy"
        o = "ay"
        self.assertEqual(s.removeDuplicates(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)