# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

from functools import cache
from collections import defaultdict
import bisect

class Solution:
    # time limit exceeded (83/87 test cases)
    def maxEnvelopes_timeout(self, envelopes: List[List[int]]) -> int:
        dp = [1] * len(envelopes)
        envelopes.sort(reverse = True)
        for i in range(1, len(envelopes)):
            w,h = envelopes[i]
            for j in range(i):
                a,b = envelopes[j]
                if a > w and b > h:
                    dp[i] = max(dp[i], 1 + dp[j])
        return max(dp)

    # time limit exceeded (82/87 test cases)
    # attempt to add binary search
    def maxEnvelopes_cached_timeout(self, envelopes: List[List[int]]) -> int:
        # sort: width large -> small and height small -> large
        envelopes.sort(key=lambda x: (-x[0], x[1]))
        d = defaultdict(list)
        for i, j in envelopes:
            d[i].append(j)
        widths = list(d.keys())
        if len(d) < 2:
            return 1
        @cache
        def sub(wIndex, height):
            # base case
            if wIndex == 0:
                return 1
            # loop through all larger widths
            b = 1
            for i in range(wIndex - 1, -1, -1):
                w = widths[i]
                # binary search
                h = bisect.bisect(d[w], height)
                if h < len(d[w]):
                    b = max(b, 1 + sub(i, d[w][h]))
                pass
            return b
        return max([sub(i, d[j][0]) for i,j in enumerate(widths)])

    '''
    Following solutions are related to longest increasing subsequence
    problem.
    https://leetcode.com/problems/longest-increasing-subsequence/
    '''

    # https://leetcode.com/problems/russian-doll-envelopes/discuss/82796/A-Trick-to-solve-this-problem.
    # comment by Merciless
    def maxEnvelopes_Merciless(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x:(x[0],-x[1]))
        n = [h for _, h in envelopes]
        l = []
        for c in n:
            i = bisect.bisect_left(l, c)
            l[i:i+1] = [c]
        return len(l)

    # https://leetcode.com/problems/russian-doll-envelopes/discuss/82796/A-Trick-to-solve-this-problem.
    # comment by leihao1313
    def maxEnvelopes_leihao1313(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x:(x[0],-x[1]))
        r = [10**5 + 1] * len(envelopes)
        for w, h in envelopes:
            r[bisect.bisect_left(r, h)] = h
        return bisect.bisect_left(r, 10**5 + 1)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[5,4],[6,4],[6,7],[2,3]]
        o = 3
        self.assertEqual(s.maxEnvelopes(i), o)

    def test_two(self):
        s = Solution()
        i = [[1,1],[1,1],[1,1]]
        o = 1
        self.assertEqual(s.maxEnvelopes(i), o)

    def test_three(self):
        s = Solution()
        i = [[2,1],[2,2],[2,3],[2,5],[1,2]]
        o = 2
        self.assertEqual(s.maxEnvelopes(i), o)

    def test_four(self):
        s = Solution()
        i = [[1,3],[3,5],[6,7],[6,8],[8,4],[9,5]]
        o = 3
        self.assertEqual(s.maxEnvelopes(i), o)

    def test_five(self):
        s = Solution()
        i = [[1,3],[9,5]]
        o = 2
        self.assertEqual(s.maxEnvelopes(i), o)

    def test_six(self):
        s = Solution()
        i = [[2,100],[3,200],[4,300],[5,500],[5,400],[5,250],[6,370],[6,360],[7,380]]
        o = 5
        self.assertEqual(s.maxEnvelopes(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)