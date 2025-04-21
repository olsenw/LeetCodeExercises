# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 0-indexed array of n integers differences, which describes the
    differences between each pair of consecutive integers of a hidden sequence
    of length (n + 1). More formally, call the hidden sequence hidden, then
    differences[i] = hidden[i + 1] - hidden[i].

    Also given are two integers lower and upper that describe the inclusive
    range of values [lower, upper] that the hidden sequence cat contain.

    Return the number of possible hidden sequences there are. If there are no
    possible sequences, return 0.
    '''
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        high, low, s = 0, 0, 0
        for d in differences:
            s += d
            high = max(high, s)
            low = min(low, s)
        if upper - lower < high - low:
            return 0
        return (upper - high) - (lower - low) + 1

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,-3,4]
        j = 1
        k = 6
        o = 2
        self.assertEqual(s.numberOfArrays(i,j,k), o)

    def test_two(self):
        s = Solution()
        i = [3,-4,5,1,-2]
        j = -4
        k = 5
        o = 4
        self.assertEqual(s.numberOfArrays(i,j,k), o)

    def test_three(self):
        s = Solution()
        i = [4,-7,2]
        j = 3
        k = 6
        o = 0
        self.assertEqual(s.numberOfArrays(i,j,k), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)