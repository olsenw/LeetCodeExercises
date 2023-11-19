# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums, make all elements in nums equal. To complete
    one operation follow these steps:
    1) Find the largest value in nums. Let its index be i (0-indexed) and its
       value be largest. If there are multiple elements with the largest value,
       pick the smallest i.
    2) Find the nex largest value in nums strictly smaller than largest. Let its
       value be nextLargest.
    3) Reduce nums[i] to nextLargest.
    
    Return the number of operations to make all elements in nums equal.
    '''
    def reductionOperations(self, nums: List[int]) -> int:
        answer = 0
        nums.sort(reverse=True)
        for i in range(1, len(nums)):
            if nums[i - 1] - nums[i] > 0:
                answer += i
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [5,1,3]
        o = 3
        self.assertEqual(s.reductionOperations(i), o)

    def test_two(self):
        s = Solution()
        i = [1,1,1]
        o = 0
        self.assertEqual(s.reductionOperations(i), o)

    def test_three(self):
        s = Solution()
        i = [1,1,2,2,3]
        o = 4
        self.assertEqual(s.reductionOperations(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)