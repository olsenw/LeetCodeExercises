# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import Counter, List, Dict, Set, Optional

class Solution:
    '''
    Given a string s and an integer k, partition s into k substrings such that
    the letter changes needed to make each substring semi-palindrome are
    minimized.

    Return the minimum number of letter changes required.

    A semi-palindrome is a special type of string that can be divided into
    palindromes based on a repeating pattern. To check if a string is a
    semi-palindrome:
    1. Choose a positive divisor d of the string's length. d can range from 1 up
       to, but not including, the string's length. For a string of length 1, it
       does not have a valid divisor as per this definition, since the only
       divisor is its length, which is not allowed.
    2. For a given divisor d, divide the string into groups where each group
       contains characters from the string that follows a repeating pattern of
       length d. Specifically, the first group consists of characters at
       positions 1, 1+d, 1+2d, and so on, the second group includes characters
       at positions 2,2+d,2+2d, etc.
    3. The string is considered a semi-palindrome if each of these groups forms
       a palindrome.
    '''
    # based on hints
    def minimumChanges_incomplete(self, s: str, k: int) -> int:
        def changes(s:str) -> int:
            a = float('inf')
            n = len(s)
            for d in range(2, n+1):
                if n % d != 0:
                    continue
                for i in range(n//d):
                    c = Counter()
                    for j in range(d):
                        c[s[i+j*d]] += 1
                    a = min(a, n - c.most_common(1)[1])
            return a
        n = len(s)
        changes("abcabc")
        # precalculate number of changes needed for substrings to become semi-palindrome
        v = [[float('inf') * n] for _ in range(n)]
        for i in range(n):
            for j in range(i+1, n):
                v[i][j] = changes(s[i:j+1])
        return

    # based on solution by Aleksandr
    # https://leetcode.com/problems/minimum-changes-to-make-k-semi-palindromes/solutions/8615226/think-in-blocks-not-groups-peel-pairs-cu-ad2d/?envType=daily-question&envId=2026-11-17
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        # every divisor for a given give length
        divisors = [[] for _ in range(n+1)]
        for d in range(1,n):
            for length in range(2*d,n+1,d):
                divisors[length].append(d)
        # split s[i:j] in blocks of length d, and find differences
        @cache
        def peel(i:int, j:int, d:int) -> int:
            if j - i <= d:
                # no blocks or single block
                # ie nothing to pair
                return 0
            answer = 0
            for a,b in zip(s[i:i+d], s[j-d:j]):
                answer += a != b
            return answer + peel(i + d, j - d, d)
        # calculate the number of changes needed to make s[i:j] semi-palindromic
        @cache
        def cost(i:int, j:int) -> int:
            return min(peel(i,j,d) for d in divisors[j-i])
        # smallest number of changes for s[:j]
        best = {0:0}
        for pieces in range(1,k):
            room = range(2 * pieces, n - 2 * (k - pieces) + 1)
            best = {j:min(best[i] + cost(i,j) for i in best if i <= j - 2) for j in room}
        return min(best[i] + cost(i,n) for i in best)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "abcac"
        j = 2
        o = 1
        self.assertEqual(s.minimumChanges(i,j), o)

    def test_two(self):
        s = Solution()
        i = "abcdef"
        j = 2
        o = 2
        self.assertEqual(s.minimumChanges(i,j), o)

    def test_three(self):
        s = Solution()
        i = "aabbaa"
        j = 3
        o = 0
        self.assertEqual(s.minimumChanges(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)