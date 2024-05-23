# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import defaultdict
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an array nums of positive integers and a positive integer k.

    A subset of nums is beautiful if it does not contain two integers with an
    absolute difference equal to k.

    Return the number of non-empty beautiful subsets of the array nums.

    A subset of nums is an array that can be obtained by deleting some (possibly
    none) elements from nums. Two subsets are different if and only if the
    chosen indices to delete are different.
    '''
    # time limit exceeded
    def beautifulSubsets_tle(self, nums: List[int], k: int) -> int:
        n = len(nums)
        answer = 0
        @cache
        def subset(choices:int) -> int:
            if choices == 0:
                return 0
            nonlocal answer
            valid = 1
            for i in range(n):
                if choices & (1 << i):
                    for j in range(i+1,n):
                        if choices & (1 << j) and abs(nums[i] - nums[j]) == k:
                            valid = 0
                            break
                    subset(choices ^ (1 << i))
            answer += valid
            return valid
        subset((1<<n) - 1)
        return answer

    def beautifulSubsets_tle2(self, nums: List[int], k: int) -> int:
        n = len(nums)
        answer = 0
        dp = set([0])
        def subset(choices:int):
            if choices in dp:
                return
            dp.add(choices)
            nonlocal answer
            valid = 1
            for i in range(n):
                if choices & (1 << i) == 0:
                    continue
                choice = choices ^ (1 << i)
                if choice not in dp:
                    subset(choice)
                for j in range(i, n):
                    if choices & (1 << j) and abs(nums[i] - nums[j]) == k:
                        valid = 0
                        break
            answer += valid
        subset((1<<n) - 1)
        return answer

    # optimized Leetcode editorial answer O(n log n)
    # https://leetcode.com/problems/the-number-of-beautiful-subsets/editorial/?envType=daily-question&envId=2024-05-23
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        total_count = 1
        freq_map = defaultdict(dict)

        # Calculate frequencies based on remainder
        for num in nums:
            freq_map[num % k][num] = freq_map[num % k].get(num, 0) + 1

        # Iterate through each remainder group
        for fr in freq_map.values():
            prev_num, curr, prev1, prev2 = -k, 1, 1, 0

            # Iterate through each number in the current remainder group
            for num, freq in sorted(fr.items()):
                # Count of subsets skipping the current number
                skip = prev1  

                # Count of subsets including the current number
                # Check if the current number and the previous number 
                # form a beautiful pair
                if num - prev_num == k:
                    take = ((1 << freq) - 1) * prev2
                else:
                    take = ((1 << freq) - 1) * prev1

                # Store the total count for the current number
                curr = skip + take  
                prev2, prev1 = prev1, curr
                prev_num = num
            total_count *= curr
        return total_count - 1

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [2,4,6]
        j = 2
        o = 4
        self.assertEqual(s.beautifulSubsets(i,j), o)

    def test_two(self):
        s = Solution()
        i = [1]
        j = 1
        o = 1
        self.assertEqual(s.beautifulSubsets(i,j), o)

    def test_three(self):
        s = Solution()
        i = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        j = 1
        o = 17710
        self.assertEqual(s.beautifulSubsets(i,j), o)

    def test_four(self):
        s = Solution()
        i = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        j = 2
        o = 20735
        self.assertEqual(s.beautifulSubsets(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)