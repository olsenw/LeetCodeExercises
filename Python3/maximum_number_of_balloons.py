# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import Counter, List, Dict, Set, Optional

class Solution:
    '''
    Given a string text, using the characters of text to form as many instances
    of the word "balloon" as possible.

    Each character in text can be used at most once. Return the maximum number
    of instances that can be formed.
    '''
    def maxNumberOfBalloons(self, text: str) -> int:
        c = Counter(text)
        b = Counter("balloon")
        return min(c[i] // b[i] for i in b)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "nlaebolko"
        o = 1
        self.assertEqual(s.maxNumberOfBalloons(i), o)

    def test_two(self):
        s = Solution()
        i = "loonbalxballpoon"
        o = 2
        self.assertEqual(s.maxNumberOfBalloons(i), o)

    def test_three(self):
        s = Solution()
        i = "leetcode"
        o = 0
        self.assertEqual(s.maxNumberOfBalloons(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)