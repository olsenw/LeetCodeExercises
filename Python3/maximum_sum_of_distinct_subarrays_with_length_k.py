# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import Counter, List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums and an integer k. Find the maximum subarray sum
    of all the subarrays of nums that meet the following conditions:
    * The length of the subarray is k, and
    * All the elements of the subarray are distinct.

    Return the maximum subarray sum of all the subarrays that meet the
    conditions. If no subarray meets the conditions, return 0.
    '''
    def maximumSubarraySum_tle(self, nums: List[int], k: int) -> int:
        answer = 0
        c = Counter(nums[:k-1])
        s = sum(nums[:k-1])
        for i in range(k-1, len(nums)):
            c[nums[i]] += 1
            s += nums[i]
            if c.most_common(1)[0][1] == 1:
                answer = max(answer, s)
            c[nums[i-k+1]] -= 1
            s -= nums[i-k+1]
        return answer
    
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        answer = 0
        s = sum(nums[:k-1])
        c = Counter()
        once = set()
        for n in nums[:k-1]:
            c[n] += 1
            if c[n] == 1:
                once.add(n)
            else:
                once.discard(n)
        for i in range(k-1, len(nums)):
            n = nums[i]
            s += n
            c[n] += 1
            if c[n] == 1:
                once.add(n)
            else:
                once.discard(n)
            if len(once) == k:
                answer = max(answer, s)
            n = nums[i-k+1]
            s -= n
            c[n] -= 1
            if c[n] == 1:
                once.add(n)
            else:
                once.discard(n)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,5,4,2,9,9,9]
        j = 3
        o = 15
        self.assertEqual(s.maximumSubarraySum(i,j), o)

    def test_two(self):
        s = Solution()
        i = [4,4,4]
        j = 3
        o = 0
        self.assertEqual(s.maximumSubarraySum(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)