# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array cookies, where cookies[i] denotes the number of
    cookies in the ith bag. Also given is an integer k that denotes the number
    of children to distribute all the bags of cookies to. All the cookies in the
    same bag must go to the same child and cannot be split up.

    The unfairness of a distribution is defined as the maximum total cookies
    obtained by a single child in the distribution.

    Return the minimum unfairness of all distributions.
    '''
    # memory limit exceeded (27/38)
    def distributeCookies_memory(self, cookies: List[int], k: int) -> int:
        @cache
        def dp(i=0, a=0,b=0,c=0,d=0,e=0,f=0,g=0,h=0):
            if i == len(cookies):
                return max(a,b,c,d,e,f,g,h)
            m = dp(i+1, a+cookies[i],b,c,d,e,f,g,h)
            m = min(m, dp(i+1, a,b+cookies[i],c,d,e,f,g,h))
            if k >= 3:
                m = min(m, dp(i+1, a,b,c+cookies[i],d,e,f,g,h))
            if k >= 4:
                m = min(m, dp(i+1, a,b,c,d+cookies[i],e,f,g,h))
            if k >= 5:
                m = min(m, dp(i+1, a,b,c,d,e+cookies[i],f,g,h))
            if k >= 6:
                m = min(m, dp(i+1, a,b,c,d,e,f+cookies[i],g,h))
            if k >= 7:
                m = min(m, dp(i+1, a,b,c,d,e,f,g+cookies[i],h))
            if k == 8:
                m = min(m, dp(i+1, a,b,c,d,e,f,g,h+cookies[i]))
            return m
        return dp()

    # based on solution by Leetcode
    # had idea for backtracking, but not early termination
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        n = len(cookies)
        children = [0] * k
        # sadChildren is the number of children without cookies
        def dfs(i, sadChildren):
            # invalid states because there are children without cookies
            if n - i < sadChildren:
                return 10**6
            if i == n:
                return max(children)
            answer = 10**6
            for j in range(k):
                if children[j] == 0:
                    sadChildren -= 1
                children[j] += cookies[i]
                answer = min(answer, dfs(i+1, sadChildren))
                children[j] -= cookies[i]
                if children[j] == 0:
                    sadChildren += 1
            return answer
        return dfs(0,k)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [8,15,10,20,8]
        j = 2
        o = 31
        self.assertEqual(s.distributeCookies(i,j), o)

    def test_two(self):
        s = Solution()
        i = [6,1,3,2,2,4,1,2]
        j = 3
        o = 7
        self.assertEqual(s.distributeCookies(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)