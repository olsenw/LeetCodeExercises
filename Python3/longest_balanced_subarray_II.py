# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import defaultdict, deque
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums.

    A subarray is called balanced in the number of distinct even numbers is
    equal to the number distinct odd numbers.

    Return the length of the longest balanced subarray.
    '''
    # based on Leetcode Editorial
    # https://leetcode.com/problems/longest-balanced-subarray-ii/editorial/?envType=daily-question&envId=2026-02-11
    # Prefix sum + segment tree
    def longestBalanced(self, nums: List[int]) -> int:
        class LazyTag:
            def __init__(self):
                self.toAdd = 0
            def add(self, other):
                self.toAdd += other.toAdd
                return self
            def hasTag(self):
                return self.toAdd != 0
            def clear(self):
                self.toAdd = 0
        class SegmentTreeNode:
            def __init__(self):
                self.minValue = 0
                self.maxValue = 0
                self.lazyTag = LazyTag()
        class SegmentTree:
            def __init__(self, data):
                self.n = len(data)
                self.tree = [SegmentTreeNode() for _ in range(self.n * 4 + 1)]
                self._build(data, 1, self.n, 1)
            def add(self, l, r, val):
                tag = LazyTag()
                tag.toAdd = val
                self._update(l, r, tag, 1, self.n, 1)
            def findLast(self, start, val):
                if start > self.n:
                    return -1
                return self._find(start, self.n, val, 1, self.n, 1)
            def _applyTag(self, i, tag):
                self.tree[i].minValue += tag.toAdd
                self.tree[i].maxValue += tag.toAdd
                self.tree[i].lazyTag.add(tag)
            def _pushDown(self, i):
                if self.tree[i].lazyTag.hasTag():
                    tag = LazyTag()
                    tag.toAdd = self.tree[i].lazyTag.toAdd
                    self._applyTag(i << 1, tag)
                    self._applyTag((i << 1) | 1, tag)
                    self.tree[i].lazyTag.clear()
            def _pushUp(self, i):
                self.tree[i].minValue = min(self.tree[i << 1].minValue, self.tree[(i << 1) | 1].minValue)
                self.tree[i].maxValue = max(self.tree[i << 1].maxValue, self.tree[(i << 1) | 1].maxValue)
            def _build(self, data, l, r, i):
                if l == r:
                    self.tree[i].minValue = data[l - 1]
                    self.tree[i].maxValue = data[l - 1]
                    return
                mid = l + ((r - l) >> 1)
                self._build(data, l, mid, i << 1)
                self._build(data, mid+1, r, (i << 1) | 1)
                self._pushUp(i)
            def _update(self, targetL, targetR, tag, l, r, i):
                if targetL <= l and r <= targetR:
                    self._applyTag(i, tag)
                    return
                self._pushDown(i)
                mid = l + ((r - l) >> 1)
                if targetL <= mid:
                    self._update(targetL, targetR, tag, l, mid, i << 1)
                if targetR > mid:
                    self._update(targetL, targetR, tag, mid + 1, r, (i << 1) | 1)
                self._pushUp(i)
            def _find(self, targetL, targetR, val, l, r, i):
                if self.tree[i].minValue > val or self.tree[i].maxValue < val:
                    return -1
                if l == r:
                    return l
                self._pushDown(i)
                mid = l + ((r - l) >> 1)
                if targetR >= mid + 1:
                    answer = self._find(targetL, targetR, val, mid + 1, r, (i << 1) | 1)
                    if answer != -1:
                        return answer
                if l <= targetR and mid >= targetL:
                    return self._find(targetL, targetR, val, l, mid, i << 1)
                return -1
        occurrences = defaultdict(deque)
        def sgn(x):
            return 1 if x % 2 == 0 else -1
        length = 0
        prefixSum = [0] * len(nums)
        prefixSum[0] = sgn(nums[0])
        occurrences[nums[0]].append(1)
        for i in range(1, len(nums)):
            prefixSum[i] = prefixSum[i-1]
            o = occurrences[nums[i]]
            if not o:
                prefixSum[i] += sgn(nums[i])
            o.append(i + 1)
        seg = SegmentTree(prefixSum)
        for i in range(len(nums)):
            length = max(length, seg.findLast(i + length, 0) - i)
            nextPos = len(nums) + 1
            occurrences[nums[i]].popleft()
            if occurrences[nums[i]]:
                nextPos = occurrences[nums[i]][0]
            seg.add(i + 1, nextPos - 1, -sgn(nums[i]))
        return length

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [2,5,4,3]
        o = 4
        self.assertEqual(s.longestBalanced(i), o)

    def test_two(self):
        s = Solution()
        i = [3,2,2,5,4]
        o = 5
        self.assertEqual(s.longestBalanced(i), o)

    def test_three(self):
        s = Solution()
        i = [1,2,3,2]
        o = 3
        self.assertEqual(s.longestBalanced(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)