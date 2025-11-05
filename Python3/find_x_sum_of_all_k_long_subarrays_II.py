# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import defaultdict
import heapq
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import Counter, List, Dict, Set, Optional

from sortedcontainers import SortedList, SortedSet

class Solution:
    '''
    Given an array nums of n integers and two integers k and x.

    The x-sum of an array is calculated by the following procedure:
    * Count the occurrences of all elements in the array.
    * Keep only the occurrences of the top x most frequent elements. If two
      elements have the same number of occurrences, the element with the bigger
      value is considered more frequent.
    * Calculate the sum of the resulting array.

    Note that if an array has less than x distinct elements, its x-sum is the
    sum of the resulting array.

    Return an integer array answer of length n - k + 1 where answer[i] is the
    x-sum of the subarray nums[i..i + k - 1].
    '''
    def findXSum_tle(self, nums: List[int], k: int, x: int) -> List[int]:
        count = Counter(nums[:k-1])
        heap = [(-count[i],-i) for i in count]
        heapq.heapify(heap)
        answer = []
        for i in range(k-1,len(nums)):
            n = nums[i]
            count[n] += 1
            heapq.heappush(heap, (-count[n],-n))
            a = 0
            h = []
            s = set()
            while heap and len(h) < x:
                countNum,num = heapq.heappop(heap)
                if num not in s and count[-num] == -countNum:
                    s.add(num)
                    a += -countNum * -num
                    h.append((countNum,num))
            answer.append(a)
            n = nums[max(0, i-k+1)]
            count[n] -= 1
            for j in h:
                if count[-j[1]] == -j[0]:
                    heapq.heappush(heap, j)
            if count[n] == 0:
                del count[n]
            else:
                heapq.heappush(heap, (-count[n],-n))
        return answer

    # based on hints
    # not enough brain to do it
    def findXSum_giveup(self, nums: List[int], k: int, x: int) -> List[int]:
        answer = []
        c = Counter(nums[:k-1])
        xMaxSet = SortedSet(key=lambda x: c[x])
        lessSet = SortedSet(key=lambda x: c[x])
        s = 0
        for i,j in c.most_common():
            if len(xMaxSet) < x:
                xMaxSet.add(i)
                s += i * j
            else:
                lessSet.add(i)
        for i in range(k-1, len(nums)):
            n = nums[i]
            c[n] += 1
            if n in xMaxSet:
                xMaxSet.remove(n)
                xMaxSet.add(n)
            else:
                les
            pass
        return answer

    # based on Leetcode editorial
    # https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-ii/editorial/?envType=daily-question&envId=2025-11-05
    # abstracts the data structure into a helper class
    # keeps track of x most frequent, less frequent, and current sum
    # also has logic for adding/removing values
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        class Helper:
            def __init__(self, size):
                self.size = size
                self.result = 0
                self.large = SortedList()
                self.small = SortedList()
                self.freq = defaultdict(int)
            def insert(self, num):
                if self.freq[num] > 0:
                    self._remove((self.freq[num], num))
                self.freq[num] += 1
                self._insert((self.freq[num], num))
            def remove(self, num):
                self._remove((self.freq[num], num))
                self.freq[num] -= 1
                if self.freq[num] > 0:
                    self._insert((self.freq[num], num))
            def get(self):
                return self.result
            def _insert(self, p):
                if len(self.large) < self.size or p > self.large[0]:
                    self.result += p[0] * p[1]
                    self.large.add(p)
                    if len(self.large) > self.size:
                        toRemove = self.large[0]
                        self.result -= toRemove[0] * toRemove[1]
                        self.large.remove(toRemove)
                        self.small.add(toRemove)
                else:
                    self.small.add(p)
            def _remove(self, p):
                if p >= self.large[0]:
                    self.result -= p[0] * p[1]
                    self.large.remove(p)
                    if self.small:
                        toAdd = self.small[-1]
                        self.result += toAdd[0] * toAdd[1]
                        self.small.remove(toAdd)
                        self.large.add(toAdd)
                else:
                    self.small.remove(p)
        helper = Helper(x)
        answer = []
        for i in range(len(nums)):
            helper.insert(nums[i])
            if i >= k:
                helper.remove(nums[i-k])
            if i >= k - 1:
                answer.append(helper.get())
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,1,2,2,3,4,2,3]
        j = 6
        k = 2
        o = [6,10,12]
        self.assertEqual(s.findXSum(i,j,k), o)

    def test_two(self):
        s = Solution()
        i = [3,8,7,8,7,5]
        j = 2
        k = 2
        o = [11,15,15,15,12]
        self.assertEqual(s.findXSum(i,j,k), o)

    def test_three(self):
        s = Solution()
        i = [5,7,9,9,6]
        j = 5
        k = 1
        o = [18]
        self.assertEqual(s.findXSum(i,j,k), o)

    def test_four(self):
        s = Solution()
        i = [2,6,4,2,3,2,5,5,1,5,6]
        j = 4
        k = 3
        o = [14,13,11,12,15,13,16,17]
        self.assertEqual(s.findXSum(i,j,k), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)