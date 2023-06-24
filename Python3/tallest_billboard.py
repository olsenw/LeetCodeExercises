# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    There is a billboard being installed at the tallest height possible. The
    billboard will have two steel supports, one on each side. Each steel support
    must be an equal height.

    Given a collection of rods that can be welded together.

    Return the largest possible height for the billboard installation. If the
    billboard cannot be supported return 0.
    '''
    # based on LeetCode dp solution... dark magics abound
    # O(n m) time where n is input array of rods and m is maximum sum of rods
    # O(m) space
    # log of subtle logic to make this work (how the dp is updated such that
    # tallest is represented preventing inferior duplicates)
    def tallestBillboard(self, rods: List[int]) -> int:
        dp = {0:0}
        for r in rods:
            # copying implicitly covers the case of not taking this rod
            np = dp.copy()
            for diff, taller in dp.items():
                shorter = taller - diff
                # case of adding the rod to the taller stand
                np[diff + r] = max(np.get(diff + r, 0), taller + r)
                # case of adding the rod to the shorted stand
                ndiff = abs(shorter + r - taller)
                ntall = max(shorter + r, taller)
                np[ndiff] = max(np.get(ndiff, 0), ntall)
            dp = np
        return dp.get(0, 0)

    '''
    Other solutions included brute force all combinations of rods
    (beam 1, beam 2, unused) and finding cases that work
    O(3^n) time

    There was a way to split problem in half and combine...
    O(3^(n/2)) time
    '''

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,3,6]
        o = 6
        self.assertEqual(s.tallestBillboard(i), o)

    def test_two(self):
        s = Solution()
        i = [1,2,3,4,5,6]
        o = 10
        self.assertEqual(s.tallestBillboard(i), o)

    def test_three(self):
        s = Solution()
        i = [1,2]
        o = 0
        self.assertEqual(s.tallestBillboard(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)