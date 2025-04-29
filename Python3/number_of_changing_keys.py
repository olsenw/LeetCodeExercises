# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 0-indexed string s typed by a user. Changing a key is defined as
    using a key different from the last used key.

    Return the number of times the user had to change the key.

    Note: Modifiers like shift or caps lock won't be counted in changing the key
    that is if a user typed the letter 'a' and then the letter 'A; then it will
    not be considered as a changing of key.
    '''
    def countKeyChanges(self, s: str) -> int:
        answer = 0
        last = s[0].lower()
        for c in s.lower()[1:]:
            if last != c:
                last = c
                answer += 1
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "aAbBcC"
        o = 2
        self.assertEqual(s.countKeyChanges(i), o)

    def test_two(self):
        s = Solution()
        i = "AaAaAaaA"
        o = 0
        self.assertEqual(s.countKeyChanges(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)