# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

from sortedcontainers import SortedList

class Solution:
    '''
    Given a 0-indexed string s. Also given a 0-indexed string queryCharacters of
    length k and a 0-indexed array of integer indices queryIndices of length k,
    both of which are used to describe k queries.

    The ith query updates the character in s at index queryIndices[i] to the
    character queryCharacters[i].

    Return an array lengths of length k where lengths[i] is the length of the
    longest substring of s consisting of only one repeating character after the
    ith query is performed.
    '''
    # O(m * n) time
    def longestRepeating_brute(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        answer = []
        s = list(s)
        for i,j in zip(queryIndices, queryCharacters):
            s[i] = j
            ans = 0
            a = 0
            b = ' '
            for x in s:
                if x == b:
                    a += 1
                else:
                    ans = max(ans, a)
                    a = 1
                    b = x
            answer.append(max(ans, a))
        return answer

    # based on Leetcode ordered set editorial
    # https://leetcode.com/problems/longest-substring-of-one-repeating-character/editorial/?envType=daily-question&envId=2026-08-13
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        n = len(s)
        s = list(s)
        segments = SortedList()
        lengths = SortedList()
        # get initial lengths of segements
        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            segments.add((i, j-1))
            lengths.add(j-i)
            i = j
        # process queries
        k = len(queryIndices)
        answer = []
        for p,c in zip(queryIndices, queryCharacters):
            # need to split a section
            if s[p] != c:
                i = segments.bisect_right((p,n)) - 1
                left, right = segments[i]
                segments.pop(i)
                lengths.remove(right - left + 1)
                if left <= p - 1:
                    segments.add((left, p - 1))
                    lengths.add(p - left)
                if p + 1 <= right:
                    segments.add((p+1, right))
                    lengths.add(right - p)
                newLeft, newRight = p,p
                if p + 1 < n and s[p+1] == c:
                    j = segments.bisect_left((p+1, -1))
                    if j < len(segments) and segments[j][0] == p + 1:
                        rightLeft,rightRight = segments[j]
                        lengths.remove(rightRight - rightLeft + 1)
                        newRight = rightRight
                        segments.pop(j)
                if p > 0 and s[p - 1] == c:
                    j = segments.bisect_right((p-1, n)) - 1
                    if j >= 0 and segments[j][1] == p - 1:
                        leftLeft, leftRight = segments[j]
                        lengths.remove(leftRight - leftLeft + 1)
                        newLeft = leftLeft
                        segments.pop(j)
                segments.add((newLeft, newRight))
                lengths.add(newRight - newLeft + 1)
                s[p] = c
            answer.append(lengths[-1])
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "babacc"
        j = "bcb"
        k = [1,3,3]
        o = [3,3,4]
        self.assertEqual(s.longestRepeating(i,j,k), o)

    def test_two(self):
        s = Solution()
        i = "abyzz"
        j = "aa"
        k = [2,1]
        o = [2,3]
        self.assertEqual(s.longestRepeating(i,j,k), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)