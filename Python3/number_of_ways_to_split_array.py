# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 0-indexed integer array nums of length n.

    nums contains a valid split at index i if the following are true:
    * The sum of the first i + 1 elements is greater than or equal to the sum of
      the last n - i - 1 elements.
    * There is at least one element to the right of i. That is, 0 <= i < n - 1.

    Return the number of valid splits in nums.
    '''
    def waysToSplitArray(self, nums: List[int]) -> int:
        answer = 0
        prefix = [nums[0]]
        for n in nums[1:]:
            prefix.append(prefix[-1] + n)
        for i in range(len(nums)-1):
            if prefix[-1] - prefix[i] <= prefix[i]:
                answer += 1
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [10,4,-8,7]
        o = 2
        self.assertEqual(s.waysToSplitArray(i), o)

    def test_two(self):
        s = Solution()
        i = [2,3,1,0]
        o = 2
        self.assertEqual(s.waysToSplitArray(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)