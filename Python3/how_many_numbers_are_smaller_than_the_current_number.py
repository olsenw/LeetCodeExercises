# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given the array nums, for each nums[i] find out how many number in the array
    are smaller than it. That is, for each nums[i] count the number of valid j's
    such that j != i and nums[j] < nums[i].

    Return the answer in an array.
    '''
    # fails
    # does not account for duplicate number in nums
    def smallerNumbersThanCurrent_fails(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [0] * n
        nums = [(j,i) for i,j in enumerate(nums)]
        for k,(j,i) in enumerate(sorted(enumerate(nums), key=lambda x:(x[1],x[0]))):
            answer[i] = k - 1
        return answer

    # Brute force
    def smallerNumbersThanCurrent_brute(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [0]*n
        for i in range(n):
            for j in range(n):
                if nums[j] < nums[i]:
                    answer[i] += 1
        return answer

    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = len(nums)
        indices = sorted(range(n), key=lambda x:nums[x])
        count = 0
        same = 1
        answer = [0] * n
        for i in range(1,n):
            if nums[indices[i]] == nums[indices[i-1]]:
                same += 1
            else:
                count += same
                same = 1
            answer[indices[i]] = count
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [8,1,2,2,3]
        o = [4,0,1,1,3]
        self.assertEqual(s.smallerNumbersThanCurrent(i), o)

    def test_two(self):
        s = Solution()
        i = [6,5,4,8]
        o = [2,1,0,3]
        self.assertEqual(s.smallerNumbersThanCurrent(i), o)

    def test_three(self):
        s = Solution()
        i = [7,7,7,7]
        o = [0,0,0,0]
        self.assertEqual(s.smallerNumbersThanCurrent(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)