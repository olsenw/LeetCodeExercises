# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an encoded string s. To decode the string to a tape, the encoded
    string is read one character at a time and the following steps are taken:
    * If the character read is a letter, that letter is written onto the tape.
    * If the character read is digit d, the entire current tape is repeatedly
      written d - 1 more time in total.
    Given an integer k, return the kth letter (1-indexed) in the decoded string.
    '''
    def decodeAtIndex_wrong(self, s: str, k: int) -> str:
        a = [["", 0]]
        for c in s:
            pass
            if c in "23456789":
                if a[-1][0] in [2,3,4,5,6,7,8,9]:
                    a[-1][0] *= int(c)
                    a[-1][1] = a[-1][0] * a[-2][1]
                else:
                    a.append([int(c), a[-1][1] * int(c)])
            else:
                if a[-1][0] in [2,3,4,5,6,7,8,9]:
                    a.append([c, a[-1][1] + 1])
                else:
                    a[-1][0] += c
                    a[-1][1] += 1
            if a[-1][1] >= k:
                break
        if isinstance(a[-1][0], str):
            while a[-1][1] > k:
                a[-1][0].pop()
                a[-1][1] -= 1
            return a[-1][0][-1]
        i = a[-1][1]
        while i > k:
            c = a.pop()[0]
            b = a.pop()[0]
            for x in range(c):
                for y in range(len(b)-1,-1,-1):
                    if i == k:
                        return b[y]
                    i -= 1
        return "a"

    def decodeAtIndex_memory_exceeded(self, s: str, k: int) -> str:
        a = ""
        for c in s:
            if c in "23456789":
                a = a * int(c)
            else:
                a = a + c
            if len(a) > k - 1:
                return a[k-1]

    # reverse traversal example by vanAmsen
    # https://leetcode.com/problems/decoded-string-at-index/solutions/4094647/97-47-reverse-traversal/?envType=daily-question&envId=2023-09-27
    def decodeAtIndex(self, s: str, k: int) -> str:
        l = 0
        i = 0
        # find length of decoded string
        # forward traversal
        while l < k:
            if s[i].isdigit():
                l *= int(s[i])
            else:
                l += 1
            i += 1
        # reverse traversal
        for j in range(i-1,-1,-1):
            c = s[j]
            if c.isdigit():
                l //= int(c)
                k %= l
            else:
                if k == 0 or k == l:
                    return c
                l -= 1

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "leet2code3"
        j = 10
        o = "o"
        self.assertEqual(s.decodeAtIndex(i,j), o)

    def test_two(self):
        s = Solution()
        i = "ha22"
        j = 5
        o = "h"
        self.assertEqual(s.decodeAtIndex(i,j), o)

    def test_three(self):
        s = Solution()
        i = "a2345678999999999999999"
        j = 1
        o = "a"
        self.assertEqual(s.decodeAtIndex(i,j), o)

    def test_four(self):
        s = Solution()
        i = "a2b3c4d5e6f7g8h9"
        j = 9
        o = "b"
        self.assertEqual(s.decodeAtIndex(i,j), o)

    def test_five(self):
        s = Solution()
        i = "cpmxv8ewnfk3xxcilcmm68d2ygc88daomywc3imncfjgtwj8nrxjtwhiem5nzqnicxzo248g52y72v3yujqpvqcssrofd99lkovg"
        j = 480551547
        o = "x"
        self.assertEqual(s.decodeAtIndex(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)