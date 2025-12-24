# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an array apple of size n and an array capacity of size m.

    There are n packs where the ith pack contains apple[i] apples. There are m
    boxes as well, and the ith box has a capacity of capacity[i] apples.

    Return the minimum number of boxes needed to select to redistribute these n
    packs of apples into boxes.

    Note that, apples from the same pack can be distributed into different
    boxes.
    '''
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        s = sum(apple)
        capacity.sort(reverse=True)
        i = 0
        while s > 0:
            s -= capacity[i]
            i += 1
        return i

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,3,2]
        j = [4,3,1,5,2]
        o = 2
        self.assertEqual(s.minimumBoxes(i,j), o)

    def test_two(self):
        s = Solution()
        i = [5,5,5]
        j = [2,4,2,7]
        o = 4
        self.assertEqual(s.minimumBoxes(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)