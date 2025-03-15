# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    There are several consecutive houses along a street, each of which has some
    money inside. There is also a robber, who wants to steal money from the
    homes, but he refuses to steal from adjacent homes.

    The capability of the robber is the maximum amount of money they steal from
    one house of all houses robbed.

    Given an integer array nums representing how much money is stashed in each
    house. More formally, the ith house from the left has nums[i] dollars.

    Return the minimum capability of the robber out of all the possible ways to
    steal at least k houses.
    '''
    # based on hints
    def minCapability(self, nums: List[int], k: int) -> int:
        def check(target:int) -> bool:
            taken = 0
            i = 0
            while i < len(nums):
                if nums[i] <= target:
                    taken += 1
                    if taken == k:
                        return True
                    i += 2
                else:
                    i += 1
            return False
        x,y = min(nums), max(nums)
        while x < y:
            z = (y-x) // 2 + x
            if check(z):
                y = z
            else:
                x = z + 1
        return x

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [2,3,5,9]
        j = 2
        o = 5
        self.assertEqual(s.minCapability(i,j), o)

    def test_two(self):
        s = Solution()
        i = [2,7,9,3,1]
        j = 2
        o = 2
        self.assertEqual(s.minCapability(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)