# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 0-indexed string blocks of length n, where blocks[i] is either 'W'
    or 'B', representing the color of the ith block. The characters 'W' and 'B'
    denote the colors white and black, respectively.

    Given an integer k, which is the desired number of consecutive black blocks.

    In one operation, it is possible to recolor a white block such that it
    becomes a black block.

    Return the minimum number of operations needed such that there is at least
    one occurrence of k consecutive black blocks.
    '''
    def minimumRecolors(self, blocks: str, k: int) -> int:
        w,b = blocks[:k].count('W'), blocks[:k].count('B')
        answer = w
        for i in range(k, len(blocks)):
            answer = min(answer, w)
            if blocks[i] == 'W':
                w += 1
            else:
                b += 1
            if blocks[i-k] == 'W':
                w -= 1
            else:
                b -= 1
        return min(answer, w)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "WBBWWBBWBW"
        j = 7
        o = 3
        self.assertEqual(s.minimumRecolors(i,j), o)

    def test_two(self):
        s = Solution()
        i = "WBWBBBW"
        j = 2
        o = 0
        self.assertEqual(s.minimumRecolors(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)