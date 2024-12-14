# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given 0-indexed integer array nums. A subarray of nums is called continuous
    if:
    * Let i, i + 1, ..., j be the indices in the subarray. Then, for each pair
      of indices i <= i1, i2 <= j, 0 <= abs(nums[i1] - nums[i2]) <= 2.

    Return the total number of continuous subarrays.

    A subarray is a contiguous non-empty sequence of elements within an array.
    '''
    # does not account all pairs, instead count sequential pairs
    def continuousSubarrays_wrong(self, nums: List[int]) -> int:
        answer = 0
        i = 0
        for j in range(1, len(nums)):
            if abs(nums[j-1] - nums[j]) > 2:
                answer += j - i + 1
                i = j
        return answer + j - i + 1

    # based on leetcode editorial
    # this works because the number of keys in frequency dict is limited to 3
    # see constraint that values are 0 <= abs(i - j) <= 2  =>  0,1,2
    def continuousSubarrays(self, nums: List[int]) -> int:
        answer = 0
        frequency = dict()
        i = 0
        for j in range(len(nums)):
            if nums[j] not in frequency:
                frequency[nums[j]] = 1
            else:
                frequency[nums[j]] += 1
            # constraint violated
            while max(frequency) - min(frequency) > 2:
                frequency[nums[i]] -= 1
                if frequency[nums[i]] == 0:
                    del frequency[nums[i]]
                i += 1
            # increment valid subsequences
            answer += j - i + 1
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [5,4,2,4]
        o = 8
        self.assertEqual(s.continuousSubarrays(i), o)

    def test_two(self):
        s = Solution()
        i = [1,2,3]
        o = 6
        self.assertEqual(s.continuousSubarrays(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)