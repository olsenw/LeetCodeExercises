# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

from collections import deque

class Solution:
    '''
    Given two strings s and t, return true if they are equal when both
    are typed into empty text editors. '#' means a backspace character.

    Note that after backspacing an empty text, the text will continue
    being empty.
    '''
    def backspaceCompare_stack(self, s: str, t: str) -> bool:
        def queue(x):
            q = deque()
            for i in x:
                if i == '#':
                    if q:
                        q.pop()
                else:
                    q.append(i)
            return q
        one = queue(s)
        two = queue(t)
        if len(one) != len(two):
            return False
        for i,j in zip(one, two):
            if i != j:
                return False
        return True

    def backspaceCompare(self, s: str, t: str) -> bool:
        def adv(string, index):
            while index >= 0 and string[index] == '#':
                a = 1
                index -= 1
                while index >= 0 and a:
                    if string[index] == '#':
                        a += 1
                    else:
                        a -= 1
                    index -= 1
            return index
        i = len(s) - 1
        j = len(t) - 1
        while True:
            i = adv(s, i)
            j = adv(t, j)
            if i == -1 and j == -1:
                return True
            elif i >= 0 and j < 0:
                return False
            elif i < 0 and j >= 0:
                return False
            elif s[i] != t[j]:
                return False
            else:
                i = i - 1 if i >= 0 else -1
                j = j - 1 if j >= 0 else -1

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "ab#c"
        j = "ad#c"
        o = True
        self.assertEqual(s.backspaceCompare(i, j), o)

    def test_two(self):
        s = Solution()
        i = "ab##"
        j = "c#d#"
        o = True
        self.assertEqual(s.backspaceCompare(i, j), o)

    def test_three(self):
        s = Solution()
        i = "a#c"
        j = "b"
        o = False
        self.assertEqual(s.backspaceCompare(i, j), o)

    def test_four(self):
        s = Solution()
        i = "xywrrmp"
        j = "xywrrm#p"
        o = False
        self.assertEqual(s.backspaceCompare(i, j), o)

    def test_five(self):
        s = Solution()
        i = "y#fo##f"
        j = "y#f#o##f"
        o = True
        self.assertEqual(s.backspaceCompare(i, j), o)

    def test_six(self):
        s = Solution()
        i = "bbbextm"
        j = "bbb#extm"
        o = False
        self.assertEqual(s.backspaceCompare(i, j), o)

    def test_seven(self):
        s = Solution()
        i = "nzp#o#g"
        j = "b#nzp#o#g"
        o = True
        self.assertEqual(s.backspaceCompare(i, j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)