# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums of even length n and an integer limit. In one
    move, it is possible to replace any integer from nums with another integer
    between 1 and limit, inclusive.

    The array nums is complementary if for all indices i (0-indexed),
    nums[i] + nums[n - 1 - i] equals the same number.

    Return the minimum number of moves required to make nums complementary.
    '''
    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        # difference array for all possible target values c
        diff = [0] * (2 * limit + 2)

        for i in range(n // 2):
            # get the minimum of the pair
            a = min(nums[i], nums[n - 1 - i])
            # get the maximum of the pair
            b = max(nums[i], nums[n - 1 - i])
            # two operations are needed (a and b are bigger than target c)
            diff[2] += 2
            # one operation needed (reduce the size of b)
            diff[a+1] -= 1
            # no operation needed (a+b = target c)
            diff[a+b] -= 1
            # one operation needed (increase size of a)
            diff[a+b+1] += 1
            # two operations needed (a and b are smaller than target c)
            diff[b+limit+1] += 1
        
        answer = n
        current = 0

        # evaluate each possible target value
        for c in range(2, 2 * limit + 1):
            current += diff[c]
            # better answer found
            if current < answer:
                answer = current

        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,4,3]
        j = 4
        o = 1
        self.assertEqual(s.minMoves(i,j), o)

    def test_two(self):
        s = Solution()
        i = [1,2,2,1]
        j = 2
        o = 2
        self.assertEqual(s.minMoves(i,j), o)

    def test_three(self):
        s = Solution()
        i = [1,2,1,2]
        j = 2
        o = 0
        self.assertEqual(s.minMoves(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)