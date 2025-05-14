# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import Counter
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string s consisting of lowercase English letters, an integer t
    representing the number of transformations to perform, and an array nums of
    size 26. In one transformation, every character in s is replaced according
    to the following rules:
    * Replace s[j] with the next nums[s[i] - 'a'] consecutive characters in the
      alphabet.
    * The transformation wraps around the alphabet if it exceeds 'z'.

    Return the length of the resulting string after exactly t transformations.

    Since the answer may be very large, return it modulo 10**9 + 7.
    '''
    m = 10**9 + 7
    def modplus(i:int,j:int):
        return ((i % Solution.m) + (j % Solution.m)) % Solution.m
    def modmul(i:int,j:int):
        return ((i % Solution.m) * (j % Solution.m)) % Solution.m
    
    # tle has for loop that can range up to 10^9...
    def lengthAfterTransformations_tle(self, s: str, t: int, nums: List[int]) -> int:
        a = list("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz")
        @cache
        def dp(c:str, t:int) -> int:
            if t == 0:
                return 1
            c = ord(c) - ord('a')
            answer = 0
            for i in range(nums[c]):
                # answer = answer + dp(a[c+i+1], t - 1)
                answer = Solution.modplus(answer, dp(a[c+i+1], t - 1))
            return answer
        c = Counter(s)
        answer = 0
        for j in range(t):
            for i in c:
                dp(i,j)
        for i in c:
            # answer = answer + (c[i] * dp(i,t))
            answer = Solution.modplus(answer, Solution.modmul(c[i], dp(i,t)))
        return answer
    
    class Mat:
        def __init__(self, copy = None):
            self.a = [[0] * 26 for _ in range(26)]
            if copy:
                for i in range(26):
                    for j in range(26):
                        self.a[i][j] = copy.a[i][j]
        def __mul__(self, other):
            result = Solution.Mat()
            for i in range(26):
                for j in range(26):
                    for k in range(26):
                        result.a[i][j] = Solution.modplus(
                            result.a[i][j],
                            Solution.modmul(self.a[i][k], other.a[k][j])
                        )
            return result
    def I() -> Mat:
        m = Solution.Mat()
        for i in range(26):
            m.a[i][i] = 1
        return m
    
    def quickmul(x: Mat, y: int) -> Mat:
        answer = Solution.I()
        cur = x
        while y:
            if y & 1:
                answer = answer * cur
            cur = cur * cur
            y >>= 1
        return answer

    # based on Leetcode editorial
    # https://leetcode.com/problems/total-characters-in-string-after-transformations-ii/editorial/?envType=daily-question&envId=2025-05-14
    # this implementation did not work but online one does
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        T = Solution.Mat()
        for i in range(26):
            for j in range(1, nums[i] + 1):
                T.a[(i + j) % 26][i] = 1
        res = Solution.quickmul(T, t)

        f = [0] * 26
        for c in s:
            f[ord(c) - ord('a')] += 1
        
        answer = 0
        for i in range(26):
            for j in range(26):
                answer = Solution.modplus(answer, Solution.modmul(res.a[i][j], f[j]))
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "abcyy"
        j = 2
        k = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2]
        o = 7
        self.assertEqual(s.lengthAfterTransformations(i,j,k), o)

    def test_two(self):
        s = Solution()
        i = "azbk"
        j = 1
        k = [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]
        o = 8
        self.assertEqual(s.lengthAfterTransformations(i,j,k), o)

    def test_three(self):
        s = Solution()
        i = "abcyy"
        j = 1000
        k = [1,1,1,1,1,1,1,1,4,1,1,1,1,1,1,5,1,1,1,1,1,1,1,1,1,2]
        o = 595260810
        self.assertEqual(s.lengthAfterTransformations(i,j,k), o)

    def test_three(self):
        s = Solution()
        i = "abcyy"
        j = 1000
        k = [1,1,1,1,1,1,1,1,4,1,1,1,1,1,1,5,1,1,1,1,1,1,1,1,1,2]
        o = 595260810
        self.assertEqual(s.lengthAfterTransformations(i,j,k), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)