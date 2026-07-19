# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import Counter, defaultdict
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string s, return the lexicographically smallest subsequence of s
    that contains all the distinct characters of s exactly once.
    '''
    def smallestSubsequence_fails(self, s: str) -> str:
        d = defaultdict()
        for i,j in enumerate(s):
            d[j] = i
        return "".join(sorted(d.keys(), key=lambda x:d[x]))

    # based on hit using masks
    def smallestSubsequence_incomplete(self, s: str) -> str:
        mask = 0
        for c in s:
            mask |= 1 << (ord(c) - ord('a'))
        subMask = 0
        stack = []
        for i,j in enumerate(s):
            m = 1 << (ord(j) - ord('a'))
            if subMask & m == 0:
                subMask |= m
                stack.append((j,i))
                continue
            moved = []
            while stack and (j,i) > stack[-1]:
                moved.append(stack.pop())
            while moved:
                stack.append
        return

    # trying for monotonic stack...
    def smallestSubsequence_fails(self, s: str) -> str:
        d = defaultdict()
        mask = 0
        stack = []
        for i,c in enumerate(s):
            m = 1 << (ord(c) - ord('a'))
            if mask & m == 0:
                mask |= m
                d[c] = i
                stack.append(c)
                continue
            pass
            while stack and stack[-1] <= c:
                stack.pop()
            if not stack:
                stack.append(c)
                d[c] = i
        return "".join(sorted(d.keys(), key=lambda x: d[x]))

    # trying for monotonic stack...
    def smallestSubsequence_fails(self, s: str) -> str:
        mask = 0
        d = defaultdict()
        stack = []
        for i in range(len(s) - 1, -1, -1):
            c = s[i]
            m = 1 << (ord(c) - ord('a'))
            # if mask & m == 0:
            #     mask |= m
            #     d[c] = i
            #     stack
            #     continue
            while stack and stack[-1] < c:
                stack.pop()
            if not stack or stack[-1] > c:
                stack.append(c)
                d[c] = i
        return "".join(sorted(d.keys(), key=lambda x: d[x]))

    def smallestSubsequence_fails(self, s: str) -> str:
        mask = 0
        d = defaultdict()
        stack = []
        for i,c in enumerate(s):
            m = 1 << (ord(c) - ord('a'))
            while stack and c < stack[-1]:
                stack.pop()
            if not stack:
                mask |= m
                mask &= (m << 1) - 1
                stack.append(c)
                d[c] = i
            elif mask & m == 0:
                mask |= m
                stack.append(c)
                d[c] = i
        return "".join(sorted(d.keys(), key=lambda x: d[x]))

    # Based on Leetcode editorial
    # https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/editorial/?envType=daily-question&envId=2026-07-19
    # make use of non-decreasing stack (monotonic stack)
    def smallestSubsequence(self, s: str) -> str:
        # know the exact counts of each letter (so know if appears later in string)
        cnt = Counter(s)
        # track if letter is already in stack (bitmask)
        mask = 0
        # monotonic stack
        stack = []
        # iterate over characters left to right
        for c in s:
            # calculate mask
            m = 1 << (ord(c) - ord('a'))
            # current letter is used, and unavailable later
            cnt[c] -= 1
            # letter in stack, skip
            if mask & m:
                continue
            # prop values off stack if
            #   larger than current letter 
            #   AND 
            #   stack letter appears again later in string
            while stack and stack[-1] > c and cnt[stack[-1]]:
                # pop from stack
                p = stack.pop()
                # remove popped letter from mask
                mask ^= 1 << (ord(p) - ord('a'))
            # append letter to stack
            stack.append(c)
            # add letter to mask
            mask |= m
        # combine stack into answer
        return "".join(stack)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "bcabc"
        o = "abc"
        self.assertEqual(s.smallestSubsequence(i), o)

    def test_two(self):
        s = Solution()
        i = "cbacdcbc"
        o = "acdb"
        self.assertEqual(s.smallestSubsequence(i), o)

    def test_three(self):
        s = Solution()
        i = "leetcode"
        o = "letcod"
        self.assertEqual(s.smallestSubsequence(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)