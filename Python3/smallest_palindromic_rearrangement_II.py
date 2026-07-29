# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import Counter
import itertools
import math
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a palindromic string s and an integer k.

    Return the kth lexicographically smallest palindromic permutation of s. If
    there are fewer than k distinct palindromic permutations, return an empty
    string.

    Note: Different rearrangements that yield the same palindromic string are
    considered identical and are counted once.
    '''
    # backtracking for distinct permutations
    # https://www.pythontutorials.net/blog/prevent-duplicates-from-itertools-permutations/#method-2-recursion-with-pruning-efficient-for-large-inputs
    # generating every answer is too slow
    def smallestPalindrome_tle(self, s: str, k: int) -> str:
        n = len(s)
        c = Counter(s[:n//2])
        center = s[n//2] if n % 2 else ""
        # permutation math based on math stack exchange
        possible = math.factorial(n // 2) // math.prod(math.factorial(c[i]) for i in c)
        if k > possible:
            return ""
        # Based on https://www.pythontutorials.net/blog/prevent-duplicates-from-itertools-permutations/#method-2-recursion-with-pruning-efficient-for-large-inputs
        answer = []
        front = sorted(s[:n//2])
        n = len(front)
        used = [False] * n
        def backtrack(current:List[str]):
            # base case
            if len(current) == n:
                answer.append(''.join(current))
                return
            for i in range(n):
                # skip if characters already used
                if used[i]:
                    continue
                # skip duplicates
                if i > 0 and front[i] == front[i-1] and not used[i-1]:
                    continue
                # mark used
                used[i] = True
                current.append(front[i])
                backtrack(current)
                current.pop()
                used[i] = False
        backtrack([])
        answer = answer[k-1]
        return answer + center + answer[::-1]

    # based on Leetcode Editorial
    # https://leetcode.com/problems/smallest-palindromic-rearrangement-ii/editorial/?envType=daily-question&envId=2026-07-29
    def smallestPalindrome(self, s: str, k: int) -> str:
        def combination(n:int, m:int, k_limit:int) -> int:
            answer = 1
            m = min(m, n-m)
            for i in range(1,m+1):
                answer *= (n-i+1) // i
                if answer > k_limit:
                    return k_limit + 1
            return answer
        partition = len(s) // 2
        bucket = [0] * 26
        for i in range(partition):
            bucket[ord(s[i]) - 97] += 1
        def permutation(rem:int) -> int:
            ways = 1
            for i in range(26):
                if bucket[i] == 0:
                    continue
                ways *= combination(rem, bucket[i], k)
                if ways > k:
                    break
                rem -= bucket[i]
            return ways
        left = []
        start = 1
        for pos in range(partition):
            for i in range(26):
                if bucket[i] == 0:
                    continue
                bucket[i] -= 1
                ways = permutation(partition - pos - 1)
                if start + ways > k:
                    left.append(chr(i+97))
                    break
                bucket[i] += 1
                start += ways
        if len(left) < partition:
            return ""
        mid = s[partition] if len(s) % 2 else ""
        left = "".join(left)
        return left + mid + left[::-1]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "abba"
        j = 2
        o = "baab"
        self.assertEqual(s.smallestPalindrome(i,j), o)

    def test_two(self):
        s = Solution()
        i = "aa"
        j = 2
        o = ""
        self.assertEqual(s.smallestPalindrome(i,j), o)

    def test_three(self):
        s = Solution()
        i = "bacab"
        j = 1
        o = "abcba"
        self.assertEqual(s.smallestPalindrome(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)