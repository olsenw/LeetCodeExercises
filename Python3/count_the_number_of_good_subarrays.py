# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import bisect
from collections import Counter
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums and an integer k, return the number of good
    subarrays of nums.

    A subarray arr is good if there are at least k pairs of indices (i,j) such
    that i < j and arr[i] == arr[j].

    A subarray is a contiguous non-empty sequence of elements within an array.
    '''
    # brute force O(n^2)
    def countGood_brute(self, nums: List[int], k: int) -> int:
        n = len(nums)
        answer = 0
        for i in range(n):
            c = Counter()
            pairs = 0
            for j in range(i, n):
                c[nums[j]] += 1
                pairs += c[nums[j]] - 1
                if pairs >= k:
                    answer += 1
        return answer

    # does not decrement pairs (works for only single value in nums)
    def countGood_fails(self, nums: List[int], k: int) -> int:
        n = len(nums)
        answer = 0
        c = Counter(nums[:1])
        pairs = [0]
        for i in range(1,n):
            c[nums[i]] += 1
            pairs.append(pairs[-1] + c[nums[i]] - 1)
        for i in range(n):
            j = bisect.bisect_left(pairs, k - pairs[i])
            if j < n and pairs[j] - pairs[i] >= k:
                answer += n - j
        return answer

    # based on Leetcode solution
    # https://leetcode.com/problems/count-the-number-of-good-subarrays/editorial/?envType=daily-question&envId=2025-04-16
    def countGood(self, nums: List[int], k: int) -> int:
        n = len(nums)
        answer = 0
        pairs = 0
        right = -1
        c = Counter()
        for left in range(n):
            while pairs < k and right + 1 < n:
                right += 1
                pairs += c[nums[right]]
                c[nums[right]] += 1
            if pairs >= k:
                answer += n - right
            c[nums[left]] -= 1
            pairs -= c[nums[left]]
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,1,1,1,1]
        j = 10
        o = 1
        self.assertEqual(s.countGood(i,j), o)

    def test_two(self):
        s = Solution()
        i = [3,1,4,3,2,2,4]
        j = 2
        o = 4
        self.assertEqual(s.countGood(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)