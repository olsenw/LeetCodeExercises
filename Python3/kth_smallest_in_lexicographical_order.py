# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import math
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given two integers n and k, return the kth lexicographically smallest
    integer in the range [1, n].
    '''
    # based on yesterdays LeetCode - 386 Lexicographical Numbers
    # the input space is large 10**9 causing time limit issues
    def findKthNumber_tle(self, n: int, k: int) -> int:
        answer = 0
        def dp(i):
            nonlocal answer
            nonlocal k
            k -= 1
            if k == 0:
                answer = i
                return
            for j in range(10):
                x = i * 10 + j
                if x > n or answer != 0:
                    break
                dp(x)
        for i in range(1,10):
            if i > n or answer != 0:
                break
            dp(i)
        return answer

    '''
    # this fails time because 10**9 is still too large for linear time
    lex = None
    # limit = 10**2
    limit = 10**9
    def dfs(self, i):
        self.lex.append(i)
        for j in range(10):
            k = i * 10 + j
            if k > self.limit:
                break
            self.dfs(k)
    def findKthNumber(self, n: int, k: int) -> int:
        if self.lex is None:
            self.lex = []
            for i in range(1,10):
                self.dfs(i)
        return self.lex[k-1]
    '''

    # faster but still too slow
    def findKthNumber_tle2(self, n: int, k: int) -> int:
        if n < 10:
            return k
        answer = 0
        def dp(i):
            nonlocal answer
            nonlocal k
            k -= 1
            if k == 0:
                answer = i
                return
            for j in range(10):
                x = i * 10 + j
                if x > n or answer != 0:
                    break
                dp(x)
            return
        i,s = n,0
        while i:
            s += 1
            i //= 10
        # s = sum(math.perm(10,i) for i in range(s))
        s = sum(10 ** i for i in range(s))
        i,k = divmod(k, s)
        # dp(i+1)
        # if k:
            # dp(i+2)
        for j in range(i+1,10):
            if answer > 0:
                break
            dp(j)
        return answer
    
    # try to further cut down on the search space iteratively pruning
    def findKthNumber_incomplete(self, n: int, k: int) -> int:
        if n < 10:
            return k
        answer = 0
        i,d = n,0
        while i:
            d += 1
            i //= 10
        l = [10 ** i for i in range(d)]
        s = sum(l)
        i,k = divmod(k,s)
        for i in range(i+1,10):
            answer = i + 1
            for x in l:
                if k < x:
                    answer += k
                    break
                k -= x
                answer *= 10
        return answer

    # based on LeetCode solution
    # https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/editorial/?envType=daily-question&envId=2024-09-22
    def findKthNumber(self, n: int, k: int) -> int:
        # helper function to calculate number of nodes range [curr, end)
        def countSteps(n, curr, end):
            steps = 0
            while curr <= n:
                steps += min(n + 1, end) - curr
                curr *= 10
                end *= 10
            return steps
        # current prefix to consider in trie
        curr = 1
        k -= 1
        while k > 0:
            steps = countSteps(n, curr, curr + 1)
            # move laterally to the next prefix in trie
            if steps <= k:
                curr += 1
                k -= steps
            # descend in the trie (current prefix correct)
            else:
                curr *= 10
                k -= 1
        return curr

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 13, 2
        o = 10
        self.assertEqual(s.findKthNumber(*i), o)

    def test_two(self):
        s = Solution()
        i = 1, 1
        o = 1
        self.assertEqual(s.findKthNumber(*i), o)

    def test_three(self):
        s = Solution()
        i = 10**9, 10**5
        o = 100089995
        self.assertEqual(s.findKthNumber(*i), o)

    def test_four(self):
        s = Solution()
        i = 21, 15
        o = 3
        self.assertEqual(s.findKthNumber(*i), o)

    def test_five(self):
        s = Solution()
        i = 5, 3
        o = 3
        self.assertEqual(s.findKthNumber(*i), o)

    def test_six(self):
        s = Solution()
        i = 804289384, 42641503
        o = 138377349
        self.assertEqual(s.findKthNumber(*i), o)

    def test_seven(self):
        s = Solution()
        i = 404, 300
        o = 369
        self.assertEqual(s.findKthNumber(*i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)