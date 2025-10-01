# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    A person is typing their name into a keyboard. Sometimes, when typing a
    character c, the key might get long pressed, and the character will be typed
    1 or more times.

    Examine the typed characters of the keyboard. Return True if it is possible
    that the person's name, with some characters (possibly none) being long
    pressed.
    '''
    # issue with trailing characters
    def isLongPressedName_fails(self, name: str, typed: str) -> bool:
        i = 0
        for t in typed:
            if t == name[i]:
                i += 1
            if i == len(name):
                return True
        return False

    def isLongPressedName_fails2(self, name: str, typed: str) -> bool:
        i = 0
        for j,t in enumerate(typed):
            if t == name[i]:
                i += 1
            if i == len(name):
                return all(name[-1] == c for c in typed[j:])
        return False

    def isLongPressedName(self, name: str, typed: str) -> bool:
        def s(x:str):
            a = [[x[0], 1]]
            for c in x[1:]:
                if c == a[-1][0]:
                    a[-1][1] += 1
                else:
                    a.append([c,1])
            return a
        name = s(name)
        typed = s(typed)
        if len(name) != len(typed):
            return False
        for i in range(len(name)):
            if not (name[i][0] == typed[i][0] and name[i][1] <= typed[i][1]):
                return False
        return True

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "alex"
        j = "aaleex"
        o = True
        self.assertEqual(s.isLongPressedName(i,j), o)

    def test_two(self):
        s = Solution()
        i = "saeed"
        j = "ssaaedd"
        o = False
        self.assertEqual(s.isLongPressedName(i,j), o)

    def test_three(self):
        s = Solution()
        i = "alex"
        j = "aaleexa"
        o = False
        self.assertEqual(s.isLongPressedName(i,j), o)

    def test_four(self):
        s = Solution()
        i = "alex"
        j = "aaleelx"
        o = False
        self.assertEqual(s.isLongPressedName(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)