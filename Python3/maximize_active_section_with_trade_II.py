# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import bisect
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a binary string s of length n, where:
    * '1' represents an active section.
    * '0' represents an inactive section.

    It is possible to perform at most one trade to maximize the number of active
    sections in s. In a trade:
    * Convert a contiguous block of '1's that is surrounded by '0's to all '0's.
    * Convert a contiguous block of '0's that is surrounded by '1's to all '1's.

    Additionally a 2D array queries is given, where queries[i] = [li, ri]
    represents a substring s[li,..ri].

    For each query, determine the maximum possible number of active sections in
    s after making the optimal trade on the substring s[li,..ri].

    Return an array answer, where answer[i] is the result for queries[i].

    Note:
    * For each query, treat s[li,..ri] as if it is augmented with a '1' at both
      ends, forming t = '1' + s[li..ri] + '1'. The augmented '1's do not
      contribute to the final count.
    * The queries are independent of each other.
    '''
    # based on Editorial
    # https://leetcode.com/problems/maximize-active-section-with-trade-ii/?envType=daily-question&envId=2026-07-22
    def maxActiveSectionsAfterTrade_incomplete(self, s: str, queries: List[List[int]]) -> List[int]:
        ones = s.count('1')
        # lengths of each contiguous zeros section
        zeroBlock = []
        zeroLeft = []
        zeroRight = []
        # counter variables for tracking
        a = s[0]
        b = 0
        l,r = 0,0
        for i,c in enumerate(s):
            if c == a:
                b += 1
                r = i
            else:
                if a == '0':
                    zeroBlock.append(b)
                    zeroLeft.append(l)
                    zeroRight.append(r)
                a = c
                b = 1
                l = i
                r = i
        answer = []
        for left, right in queries:
            l = bisect.bisect(zeroLeft, left)
            r = bisect.bisect(zeroRight,right)
            a = min(right,zeroRight[r]) - left + 1
        return answer

    # based on Editorial
    # https://leetcode.com/problems/maximize-active-section-with-trade-ii/?envType=daily-question&envId=2026-07-22
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        class SegmentTree:
            def __init__(self, arr):
                self.n = len(arr)
                self.arr = arr
                self.seg = [0] * (self.n << 2) # length times 4
                if self.n:
                    self.build(1, 0, self.n-1)
            def build(self, p:int, left:int, right:int) -> None:
                if left == right:
                    self.seg[p] = self.arr[left]
                    return
                mid = (left + right) // 2
                self.build(p * 2, left, mid)
                self.build((p * 2) | 1, mid + 1, right)
                self.seg[p] = max(self.seg[p * 2], self.seg[(p * 2) | 1])
            def query(self, left:int, right:int) -> int:
                if left > right:
                    return 0
                def _query(p:int, l:int, r:int) -> int:
                    if left <= l and r <= right:
                        return self.seg[p]
                    mid = (l + r) // 2
                    answer = 0
                    if left <= mid:
                        answer = max(answer, _query(p*2, l, mid))
                    if right > mid:
                        answer = max(answer, _query((p*2)|1, mid+1, r))
                    return answer
                return _query(1,0,self.n - 1)
        # 
        n = len(s)
        ones = s.count('1')
        zeroBlocks = []
        zeroLeft = []
        zeroRight = []
        i = 0
        while i < n:
            start = i
            while i < n and s[i] == s[start]:
                i += 1
            if s[start] == '0':
                zeroBlocks.append(i - start)
                zeroLeft.append(start)
                zeroRight.append(i-1)
        m = len(zeroBlocks)
        # less than two continuous zero blocks (ie unable to "trade")
        if m < 2:
            return[ones] * len(queries)
        tmpSum = [zeroBlocks[i] + zeroBlocks[i+1] for i in range(m-1)]
        seg = SegmentTree(tmpSum)
        answer = []
        for left,right in queries:
            i = bisect.bisect_left(zeroRight, left)
            j = bisect.bisect_right(zeroLeft, right) - 1
            # edge case, at most one continuous block of '0's in substring
            if i > m or j < 0 or i >= j:
                answer.append(ones)
                continue
            first = zeroRight[i] - max(zeroLeft[i], left) + 1
            last = min(zeroRight[j], right) - zeroLeft[j] + 1
            # exactly 2 consecutive 0 blocks within substring
            if i + 1 == j:
                answer.append(ones + first + last)
                continue
            caseLeft = first + zeroBlocks[i+1]
            caseRight = zeroBlocks[j-1] + last
            caseMid = seg.query(i+1,j-2)
            answer.append(ones + max(caseLeft,caseRight, caseMid))
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "01"
        j = [[0,1]]
        o = [1]
        self.assertEqual(s.maxActiveSectionsAfterTrade(i,j), o)

    def test_two(self):
        s = Solution()
        i = "0100"
        j = [[0,3],[0,2],[1,3],[2,3]]
        o = [4,3,1,1]
        self.assertEqual(s.maxActiveSectionsAfterTrade(i,j), o)

    def test_three(self):
        s = Solution()
        i = "1000100"
        j = [[1,5],[0,6],[0,4]]
        o = [6,7,2]
        self.assertEqual(s.maxActiveSectionsAfterTrade(i,j), o)

    def test_four(self):
        s = Solution()
        i = "01010"
        j = [[0,3],[1,4],[1,3]]
        o = [4,4,2]
        self.assertEqual(s.maxActiveSectionsAfterTrade(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)