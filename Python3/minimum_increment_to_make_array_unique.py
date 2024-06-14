# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums. In one move, pick an index i where
    0 <= i < nums.length and increment nums[i] by 1.

    Return the minimum number of moves to make every value in nums unique.

    The test cases are generated so that the answer fits in a 32-bit integer.
    '''
    def minIncrementForUnique(self, nums: List[int]) -> int:
        answer = 0
        nums.sort()
        nums.append(10**7)
        i = 0
        h = []
        for j in range(1,len(nums)):
            if nums[i] != nums[j]:
                i = nums[i] + 1
                while h and i < nums[j]:
                    answer += i - h.pop()
                    i += 1
                i = j
            else:
                h.append(nums[j])
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,2]
        o = 1
        self.assertEqual(s.minIncrementForUnique(i), o)

    def test_two(self):
        s = Solution()
        i = [3,2,1,2,1,7]
        o = 6
        self.assertEqual(s.minIncrementForUnique(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)