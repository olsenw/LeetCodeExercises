# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import heapq
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import Counter, List, Dict, Set, Optional

class Solution:
    '''
    Given two positive 0-indexed integer arrays nums1 and nums2, both of length
    n.

    The sum of squared difference of arrays nums1 and nums2 is defined as the
    sum of (nums1[i] - nums2[i])^2 for each 0 <= i < n.

    Also given two positive integers k1 and k2. It is possible to modify any of
    the elements of nums1 by +1 or -1 at most k1 times. Similarly it is possible
    to modify the elements of nums2 by +1 or -1 at most k2 times.

    Return the minimum sum of squared difference after modifying array nums1 at
    most k1 times and modifying array nums2 at most k2 times.

    Note: it is possible to modify the array elements such that they become
    negative integers.
    '''
    def minSumSquareDiff_fails(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        heap = [(-abs(j-k),i,j,k) for i,(j,k) in enumerate(zip(nums1, nums2))]
        heapq.heapify(heap)
        while (k1 > 0 or k2 > 0) and heap[0][0] < 0:
            _, i, j, k = heapq.heappop(heap)
            if k1 > k2:
                j = j + 1 if j < k else j - 1
                if k2 > 0 and j != k:
                    k = k + 1 if k < j else k - 1
            else:
                if k2 > 0 and j != k:
                    k = k + 1 if k < j else k - 1
                if k1 > 0 and j != k:
                    j = j + 1 if j < k else j - 1
            heapq.heappush(heap, (-abs(j-k), i, j, k))
        return sum(i[0] * i[0] for i in heap)

    def minSumSquareDiff_tle(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        heap = [(-abs(j-k),i,j,k) for i,(j,k) in enumerate(zip(nums1, nums2))]
        heapq.heapify(heap)
        while (k1 > 0 or k2 > 0) and heap[0][0] < 0:
            _, i, j, k = heapq.heappop(heap)
            if k1 > 0 and k1 >= k2:
                j = j + 1 if j < k else j - 1
                k1 -= 1
                pass
            elif k2 > 0 and k2 >= k1:
                k = k + 1 if k < j else k - 1
                k2 -= 1
                pass
            else:
                pass
            heapq.heappush(heap, (-abs(j-k), i, j, k))
        return sum(i[0] * i[0] for i in heap)

    # based on hints 1 and 2
    def minSumSquareDiff_tle(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        heap = [-abs(i-j) for i,j in zip(nums1,nums2)]
        heapq.heapify(heap)
        for _ in range(k1+k2):
            if heap[0] == 0:
                break
            heapq.heapreplace(heap, heap[0] + (1 if heap[0] < 0 else -1))
        return sum(i*i for i in heap)

    # based on editorial by Vaibhav Raj Singh
    # https://leetcode.com/problems/minimum-sum-of-squared-difference/solutions/8565021/easy-greedy-solution-by-rosvert-mshf/?envType=daily-question&envId=2026-10-10
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        frequency = Counter(abs(i-j) for i,j in zip(nums1, nums2))
        k = k1 + k2
        for i in range(max(frequency.keys()), 0, -1):
            if frequency[i] <= k:
                k -= frequency[i]
                frequency[i-1] += frequency[i]
                del frequency[i]
            else:
                frequency[i] -= k
                frequency[i-1] += k
                break
        return sum(frequency[i] * i * i for i in frequency)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,3,4]
        j = [2,10,20,19]
        k = 0
        l = 0
        o = 579
        self.assertEqual(s.minSumSquareDiff(i,j,k,l), o)

    def test_two(self):
        s = Solution()
        s = Solution()
        i = [1,4,10,12]
        j = [5,8,6,9]
        k = 1
        l = 1
        o = 43
        self.assertEqual(s.minSumSquareDiff(i,j,k,l), o)

    def test_three(self):
        s = Solution()
        s = Solution()
        i = [11,1,1]
        j = [1,1,1]
        k = 10
        l = 0
        o = 0
        self.assertEqual(s.minSumSquareDiff(i,j,k,l), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)