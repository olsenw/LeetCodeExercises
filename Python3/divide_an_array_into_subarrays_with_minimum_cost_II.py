# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import heapq
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import Counter, List, Dict, Set, Optional

from sortedcontainers import SortedList

class Solution:
    '''
    Given a 0-indexed array of integers nums of length n, and two positive 
    integers k and dist.

    The cost of an array is the value of its first element.

    Divide nums into k disjoint contiguous subarrays, such that the difference
    between the starting index of the second subarray and the starting index of
    the kth subarray should less than or equal to dist.

    Return the minimum possible sum of the cost of these subarrays.
    '''
    # brute force based on hints
    def minimumCost_brute(self, nums: List[int], k: int, dist: int) -> int:
        n = len(nums)
        answer = float('inf')
        for i in range(1,n-k+1):
            maxHeap = [-nums[i]]
            for j in range(i+1, min(i+dist+1, n)):
                if len(maxHeap) == k - 1:
                    heapq.heappushpop(maxHeap, -nums[j])
                else:
                    heapq.heappush(maxHeap, -nums[j])
            answer = min(answer, nums[0] - sum(maxHeap))
        return answer

    # based on hints
    def minimumCost_incomplete(self, nums: List[int], k: int, dist: int) -> int:
        n = len(nums)
        window = Counter()
        maxHeap = []
        minHeap = []
        for i in range(1,dist+2):
            window[nums[i]] += 1
            if len(maxHeap) < k - 1:
                heapq.heappush(maxHeap, -nums[i])
            elif -maxHeap[0] > nums[i]:
                heapq.heappush(minHeap, -heapq.heappushpop(maxHeap, -nums[i]))
            else:
                heapq.heappush(minHeap, nums[i])
        answer = nums[0] - sum(maxHeap)
        for i in range(2,n-k+1):
            window[nums[i + dist]] += 1
            window[nums[i - 1]] -= 1
        return answer

    # based on Leetcode editorial
    # https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-ii/editorial/?envType=daily-question&envId=2026-02-02
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        # data class to maintain two sorted lists
        # one is the k smallest elements in a window
        # other is the remaining elements in a window
        class Container:
            def __init__(self, k:int):
                self.k = k
                self.smallest = SortedList()
                self.remaining = SortedList()
                self.sum = 0
            # update sorted lists (minimum value in window)
            def adjust(self):
                while len(self.smallest) < self.k and len(self.remaining) > 0:
                    value = self.remaining[0]
                    self.smallest.add(value)
                    self.remaining.remove(value)
                    self.sum += value
                while len(self.smallest) > self.k:
                    value = self.smallest[-1]
                    self.remaining.add(value)
                    self.smallest.remove(value)
                    self.sum -= value
            def add(self, value:int):
                if len(self.remaining) > 0 and value >= self.remaining[0]:
                    self.remaining.add(value)
                else:
                    self.smallest.add(value)
                    self.sum += value
                self.adjust()
            def remove(self, value:int):
                if value in self.smallest:
                    self.smallest.remove(value)
                    self.sum -= value
                elif value in self.remaining:
                    self.remaining.remove(value)
                self.adjust()
        n = len(nums)
        container = Container(k-2)
        for i in range(1,k-1):
            container.add(nums[i])
        answer = container.sum + nums[k-1]
        # window on ending element
        # ie the starting index of the last group
        for i in range(k,n):
            j = i - dist - 1
            if j > 0:
                container.remove(nums[j])
            container.add(nums[i-1])
            answer = min(answer, container.sum + nums[i])
        return answer + nums[0]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,3,2,6,4,2]
        j = 3
        k = 3
        o = 5
        self.assertEqual(s.minimumCost(i,j,k), o)

    def test_two(self):
        s = Solution()
        i = [10,1,2,2,2,1]
        j = 4
        k = 3
        o = 15
        self.assertEqual(s.minimumCost(i,j,k), o)

    def test_three(self):
        s = Solution()
        i = [10,8,18,9]
        j = 3
        k = 1
        o = 36
        self.assertEqual(s.minimumCost(i,j,k), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)