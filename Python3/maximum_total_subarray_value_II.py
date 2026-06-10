# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import heapq
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums of length n and an integer k.

    Select exactly k distinct non-empty subarrays nums[l..r] of nums. Subarrays
    may overlap, but the exact same subarray (same l and r) cannot be chosen
    more than once.

    The value of a subarray nums[l..r] is defined as:
    max(nums[l..r]) - min(nums[l..r]).

    The total value is the sum of the values of all chosen subarrays.

    Return the maximum possible total value that can be achieved.
    '''
    # struggle too hard... keep getting caught by cases
    def maxTotalValue_fails(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # small = [(j,i) for i,j in enumerate(nums)]
        # large = [(-j,-i) for i,j in enumerate(nums)]
        small = dict()
        for i,j in enumerate(nums):
            if j in small:
                small[j] = max(small[j], i)
            else:
                small[j] = i
        large = dict()
        for i,j in enumerate(nums):
            if j in large:
                large[j] = min(large[j], i)
            else:
                large[j] = i
        small = [(i,small[i]) for i in small]
        large = [(-i,-large[i]) for i in large]
        heapq.heapify(small)
        heapq.heapify(large)
        answer = 0
        while k:
            s,i = heapq.heappop(small)
            l,j = heapq.heappop(large)
            l *= -1
            j *= -1
            if l < s:
                break
            x,y = min(i,j), max(i,j)
            t = min(k, (n - y) * (x + 1))
            answer += t * (l - s)
            k -= t
            if len(small) == 0:
                heapq.heappush(small, (s,i))
            elif len(large) == 0:
                heapq.heappush(large, (-l,-j))
            elif s - small[0][0] < l + large[0][0]:
                heapq.heappush(large, (-l,-j))
            else:
                heapq.heappush(small, (s,i))
            n = y
        return answer

    # based on LeetCode editorial
    # https://leetcode.com/problems/maximum-total-subarray-value-ii/editorial/?envType=daily-question&envId=2026-06-10
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n = len(nums)
        logn = n.bit_length()
        sparseMax = [[0] * logn for _ in range(n)]
        sparseMin = [[0] * logn for _ in range(n)]
        for i in range(n):
            sparseMax[i][0] = sparseMin[i][0] = nums[i]
        for j in range(1, logn):
            step = 1 << (j - 1)
            for i in range(n - (1 << j) + 1):
                sparseMax[i][j] = max(sparseMax[i][j-1], sparseMax[i + step][j-1])
                sparseMin[i][j] = min(sparseMin[i][j-1], sparseMin[i + step][j-1])
        def queryMax(l:int,r:int) -> int:
            j = (r - l + 1).bit_length() - 1
            return max(sparseMax[l][j], sparseMax[r - (1 << j) + 1][j])
        def queryMin(l:int,r:int) -> int:
            j = (r - l + 1).bit_length() - 1
            return min(sparseMin[l][j], sparseMin[r - (1 << j) + 1][j])
        maxHeap = [(-(queryMax(i,n-1)-queryMin(i,n-1)),i,n-1) for i in range(n)]
        heapq.heapify(maxHeap)
        answer = 0
        while k:
            val,l,r = heapq.heappop(maxHeap)
            answer -= val
            k -= 1
            if r > l:
                heapq.heappush(maxHeap, (-(queryMax(l,r-1)-queryMin(l,r-1)),l,r-1))
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,3,2]
        j = 2
        o = 4
        self.assertEqual(s.maxTotalValue(i,j), o)

    def test_two(self):
        s = Solution()
        i = [4,2,5,1]
        j = 3
        o = 12
        self.assertEqual(s.maxTotalValue(i,j), o)

    def test_three(self):
        s = Solution()
        i = [22]
        j = 1
        o = 0
        self.assertEqual(s.maxTotalValue(i,j), o)

    def test_four(self):
        s = Solution()
        i = [11,8]
        j = 2
        o = 3
        self.assertEqual(s.maxTotalValue(i,j), o)

    def test_five(self):
        s = Solution()
        i = [9,9,37]
        j = 3
        o = 56
        self.assertEqual(s.maxTotalValue(i,j), o)

    def test_six(self):
        s = Solution()
        i = [9,9,37]
        j = 6
        o = 56
        self.assertEqual(s.maxTotalValue(i,j), o)

    def test_seven(self):
        s = Solution()
        i = [18,36,6]
        j = 6
        o = 78
        self.assertEqual(s.maxTotalValue(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)