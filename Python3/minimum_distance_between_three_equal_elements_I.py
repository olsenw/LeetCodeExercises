# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import defaultdict
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums.

    A tuple (i,j,k) of 3 distinct indices is good if
    nums[i] == nums[j] == nums[k].

    The distance of a good tuple is abs(i - j) + abs(j - k) + abs(k - i), where
    abs(x) denotes the absolute value of x.

    Return an integer denoting the minimum possible distance of a good tuple. If
    no good tuple exist, return -1.
    '''
    def minimumDistance(self, nums: List[int]) -> int:
        n = len(nums)
        answer = float('inf')
        last:Dict[int,int] = dict()
        for j in range(n):
            x = nums[j]
            if x not in last:
                last[x] = j
                continue
            i = last[x]
            for k in range(j+1,n):
                if nums[k] == x:
                    answer = min(answer, abs(i-j) + abs(j-k) + abs(k-i))
            last[x] = j
        return -1 if answer == float('inf') else answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,1,1,3]
        o = 6
        self.assertEqual(s.minimumDistance(i), o)

    def test_two(self):
        s = Solution()
        i = [1,1,2,3,2,1,2]
        o = 8
        self.assertEqual(s.minimumDistance(i), o)

    def test_three(self):
        s = Solution()
        i = [1]
        o = -1
        self.assertEqual(s.minimumDistance(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)