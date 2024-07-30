# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from itertools import accumulate
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string s consisting only of characters 'a' and 'b'.

    Delete any number of characters in s to make s balanced. s is balanced if
    there are no pairs of indices (i,j) such that i < j and s[i] = 'b' and
    s[j] = 'a'.

    Return the minimum number of deletions needed to make s balanced.
    '''
    # based on hints
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        # 'a' characters to right of index
        a = [0]
        for c in s[::-1]:
            a.append(a[-1])
            if c == 'a':
                a[-1] += 1
        a.pop()
        a = a[::-1]
        # 'b' characters to left of index
        b = [0]
        for c in s:
            b.append(b[-1])
            if c == 'b':
                b[-1] += 1
        b.pop()
        # do math to find the minium number of deletions
        return min(a[i] + b[i] for i in range(n))

    def minimumDeletions_wrong(self, s: str) -> int:
        remove = False
        a = 0
        for c in s:
            if remove:
                if c == 'a':
                    a += 1
            else:
                if c == 'b':
                    remove = not remove
        remove = False
        b = 0
        for c in s[::-1]:
            if remove:
                if c == 'b':
                    b += 1
            else:
                if c == 'a':
                    remove = not remove
        return min(a,b)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "aababbab"
        o = 2
        self.assertEqual(s.minimumDeletions(i), o)

    def test_two(self):
        s = Solution()
        i = "bbaaaaabb"
        o = 2
        self.assertEqual(s.minimumDeletions(i), o)

    def test_three(self):
        s = Solution()
        i = "ababaaaabbbbbaaababbbbbbaaabbaababbabbbbaabbbbaabbabbabaabbbababaa"
        o = 25
        self.assertEqual(s.minimumDeletions(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)