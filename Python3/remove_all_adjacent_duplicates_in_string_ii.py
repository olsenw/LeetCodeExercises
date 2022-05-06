# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

from collections import deque

class Solution:
    '''
    Given a string s and an integer k, a k duplicate removal consists of
    choosing k adjacent and equal letters from s and removing them,
    causing the left and right side of the deleted substring to
    concatenate together.

    Repeatedly make k duplicate removals on s until it is no longer
    possible to make a k duplicate removal.

    Return the final string after all such duplicate removals have been
    made. It is guaranteed that the answer is unique.
    '''
    def removeDuplicates(self, s: str, k: int) -> str:
        # works because s only contains lowercase english letters, would
        # have to change ' ' to a character that could not appear in
        # input string.
        d = deque([' '])
        for i in s:
            if i == d[-1][0]:
                d[-1] += i
            else:
                d.append(i)
            if len(d[-1]) >= k:
                d.pop()
        return ''.join(d)[1:]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "abcd"
        j = 2
        o = "abcd"
        self.assertEqual(s.removeDuplicates(i,j), o)

    def test_two(self):
        s = Solution()
        i = "deeedbbcccbdaa"
        j = 3
        o = "aa"
        self.assertEqual(s.removeDuplicates(i,j), o)

    def test_three(self):
        s = Solution()
        i = "pbbcggttciiippooaais"
        j = 2
        o = "ps"
        self.assertEqual(s.removeDuplicates(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)