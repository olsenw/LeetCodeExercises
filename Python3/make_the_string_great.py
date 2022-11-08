# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given a string s of lower and upper case English letters.

    A good string is a string which doesn't have two adjacent characters s[i]
    and s[i+1] where
    * 0 <= i <= s.length - 2
    * s[i] is a lower-case letter and s[i+1] is the same letter but in
      upper-case or vice-versa.
    
    To make the string good, one may choose two adjacent characters that make
    the string bad and remove them. It is possible to do this until the string
    becomes good.

    Return the string after making is good. The answer is guaranteed to be
    unique for test cases.

    Notice that an empty string is also good.
    '''
    def makeGood(self, s: str) -> str:
        answer = []
        for c in s:
            answer.append(c)
            if len(answer) >= 2 and abs(ord(answer[-1]) - ord(answer[-2])) == 32:
                answer.pop()
                answer.pop()
        return "".join(answer)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "leEeetcode"
        o = "leetcode"
        self.assertEqual(s.makeGood(i), o)

    def test_two(self):
        s = Solution()
        i = "abBAcC"
        o = ""
        self.assertEqual(s.makeGood(i), o)

    def test_three(self):
        s = Solution()
        i = "s"
        o = "s"
        self.assertEqual(s.makeGood(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)