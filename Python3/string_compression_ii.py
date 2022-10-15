# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Run-length encoding is a string compression method that works by replacing
    consecutive identical characters (repeated 2 or more times) with the
    concatenation of the character and the number marking the count of the
    characters (length of the run). For example, to compress the string "aabccc"
    replace "aa" by "a2" and replace "ccc" by "c3". Thus the compressed string
    becomes "a2bc3".

    Notice that in this problem, the digit '1' is not added after single
    characters.

    Given a string s and an integer k, delete at most k characters from s such
    that the run-length encoded version of s has minimum length.

    Find the minimum length of the run-length encoded version of s after
    deleting at most k characters.
    '''
    # encodes the input string
    def encode(self, s):
        if len(s) == 0:
            return ""
        a = s[0]
        b = 0
        for c in s[1:]:
            if c == a[-1]:
                b += 1
            else:
                if b:
                    a += str(b+1)
                b = 0
                a += c
        if b:
            a += str(b+1)
        return a
    
    # works on small strings (too complex otherwise) [ie timeout]
    @cache
    def getLengthOfOptimalCompression_timeout(self, s: str, k: int) -> int:
        if k == 0:
            return len(self.encode(s))
        return min(self.getLengthOfOptimalCompression(s[:i] + s[i+1:], k-1) for i in range(len(s)))
    
    # based on leetcode hints... did not finish (not enough information in dp?)
    def getLengthOfOptimalCompression_unsure(self, s: str, k: int) -> int:
        # how many of same character leading and including this index
        prefix = [1] * len(s)
        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                prefix[i] += prefix[i-1]
        # i is the index in string, r is the remaining cuts
        @cache
        def dp(i,r):
            if r == 0: # what do I calc here
                return 0
            if len(s) - 1 - i == r:
                return 0 # again here
            a = dp(i+1, r-1)
            b = dp(i+1, r)
            return min(a,b)
        return dp(0,k)

    # more abstract way to represent encoding
    def getLengthOfOptimalCompression_abstract(self, s: str, k: int) -> int:
        segments = []
        a,b = s[0], 1
        for c in s[1:]:
            if c == a:
                b += 1
            else:
                segments.append((a,b))
                a,b = c, 1
        segments.append((a,b))
        def length(a,b):
            if b <= 1:
                return b
            c = 0
            while b:
                c += 1
                b //= 10
            return c + 1
        l = [length(*s) for s in segments]

    # based on discussion post by klimkina
    # https://leetcode.com/problems/string-compression-ii/discuss/755970/Python-dynamic-programming
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        # start index, last character, count of last character, removals
        @cache
        def dp(index, last, count, removals):
            # no removal available
            if removals < 0:
                # one larger than max string size
                return 101
            # ran out of string to remove characters from
            if index >= len(s):
                return 0
            # found another character same as the last
            if s[index] == last:
                # add current character to string does increase digit length
                increment = 1 if count == 1 or count == 9 or count == 99 else 0
                # no point making a removal, that would have been done when
                # current character was first seen (ie the else clause)
                return increment + dp(index+1, last, count+1, removals)
            # different character found
            else:
                # add character to string
                keep = 1 + dp(index+1, s[index], 1, removals)
                # skip character
                remove = dp(index+1, last, count, removals-1)
                # best option to minimize length
                return min(keep, remove)
        return dp(0, "", 0, k)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "aaabcccd"
        j = 2
        o = 4
        self.assertEqual(s.getLengthOfOptimalCompression(i,j), o)

    def test_two(self):
        s = Solution()
        i = "aabbaa"
        j = 2
        o = 2
        self.assertEqual(s.getLengthOfOptimalCompression(i,j), o)

    def test_three(self):
        s = Solution()
        i = "aaaaaaaaaaa"
        j = 0
        o = 3
        self.assertEqual(s.getLengthOfOptimalCompression(i,j), o)

    def test_four(self):
        s = Solution()
        i = "a" * 100
        j = 100
        o = 0
        self.assertEqual(s.getLengthOfOptimalCompression(i,j), o)

    def test_five(self):
        s = Solution()
        i = "ab" * 50
        j = 50
        o = 3
        self.assertEqual(s.getLengthOfOptimalCompression(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)