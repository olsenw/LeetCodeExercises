# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string s consisting of the characters 'a', 'b', and 'c' and a
    non-negative integer k. Each minute, it is possible to take either the
    leftmost or rightmost character of s.

    Return the minimum number of minutes needed to take at least k of each
    character, or return -1, if it is not possible to take k of each character.
    '''
    def takeCharacters_brute(self, s: str, k: int) -> int:
        if k == 0:
            return 0
        a,b,c = 0,0,0
        for i in s:
            if i == 'a':
                a += 1
            elif i == 'b':
                b += 1
            else:
                c += 1
        if a < k or b < k or c < k:
            return -1
        answer = len(s)
        a,b,c = 0,0,0
        for j in range(len(s)-1,0,-1):
            if s[j] == 'a':
                a += 1
            elif s[j] == 'b':
                b += 1
            else:
                c += 1
            x,y,z = a,b,c
            for i in range(j):
                if s[i] == 'a':
                    x += 1
                elif s[i] == 'b':
                    y += 1
                else:
                    z += 1
                if x >= k and y >= k and z >= k:
                    answer = min(answer, i + 1 + len(s) - j)
                    break
        return answer

    def takeCharacters(self, s: str, k: int) -> int:
        if k == 0:
            return 0
        a,b,c = 0,0,0
        for i in s:
            if i == 'a':
                a += 1
            elif i == 'b':
                b += 1
            else:
                c += 1
        if a < k or b < k or c < k:
            return -1
        x,y,z = 0,0,0
        j = 0
        answer = len(s)
        while j < len(s) and a+x >= k and b+y >= k and c+z >= k:
            answer = min(answer, len(s) - j)
            if s[j] == 'a':
                a -= 1
            elif s[j] == 'b':
                b -= 1
            else:
                c -= 1
            j += 1
        for i in range(len(s)):
            if s[i] == 'a':
                x += 1
            elif s[i] == 'b':
                y += 1
            else:
                z += 1
            if i == j:
                if s[i] == 'a':
                    a -= 1
                elif s[i] == 'b':
                    b -= 1
                else:
                    c -= 1
                j += 1
            pass
            while j < len(s) and a+x >= k and b+y >= k and c+z >= k:
                answer = min(answer, i + len(s) - j + 1)
                if s[j] == 'a':
                    a -= 1
                elif s[j] == 'b':
                    b -= 1
                else:
                    c -= 1
                j += 1
            if a+x >= k and b+y >= k and c+z >= k:
                answer = min(answer, i + len(s) - j + 1)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "aabaaaacaabc"
        j = 2
        o = 8
        self.assertEqual(s.takeCharacters(i,j), o)

    def test_two(self):
        s = Solution()
        i = "a"
        j = 1
        o = -1
        self.assertEqual(s.takeCharacters(i,j), o)

    def test_three(self):
        s = Solution()
        i = "a"
        j = 0
        o = 0
        self.assertEqual(s.takeCharacters(i,j), o)

    def test_four(self):
        s = Solution()
        i = "acba"
        j = 1
        o = 3
        self.assertEqual(s.takeCharacters(i,j), o)

    def test_five(self):
        s = Solution()
        i = "cbbac"
        j = 1
        o = 3
        self.assertEqual(s.takeCharacters(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)