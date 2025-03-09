# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    There is a circle of red and blue tiles. Given an array of integers colors
    and an integer k. The color of tile i is represented by colors[i].
    * colors[i] == 0 means that tile i is red.
    * colors[i] == 1 means that tile i is blue.

    An alternating group of every k contiguous tiles in the circle with
    alternating colors (each tile in the group except the first and last one has
    a different color from its left and right tiles).

    Return the number of alternating groups.

    Note that since colors represents a circle, the first and the last tiles are
    considered to be next to each other.
    '''
    def numberOfAlternatingGroups_brute(self, colors: List[int], k: int) -> int:
        n = len(colors)
        colors = colors + colors[:k]
        answer = 0
        for i in range(n):
            valid = colors[i]
            for j in range(i+1,i+k):
                if colors[j] == valid:
                    valid = -1
                    break
                valid = colors[j]
            if valid != -1:
                answer += 1
        return answer

    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
        colors = colors + colors[:k-1]
        answer = 0
        i = 0
        j = -1
        while i < len(colors):
            if j == -1:
                if i >= n or i + k - 1 >= len(colors):
                    break
                j = i + 1
                while j < i + k:
                    if colors[j-1] == colors[j]:
                        i = j
                        j = -1
                        break
                    j += 1
                if j != -1:
                    i = j
                    answer += 1
            else:
                if colors[i-1] == colors[i]:
                    j = -1
                else:
                    answer += 1
                    i += 1
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [0,1,0,1,0]
        j = 3
        o = 3
        self.assertEqual(s.numberOfAlternatingGroups(i,j), o)

    def test_two(self):
        s = Solution()
        i = [0,1,0,0,1,0,1]
        j = 6
        o = 2
        self.assertEqual(s.numberOfAlternatingGroups(i,j), o)

    def test_three(self):
        s = Solution()
        i = [1,1,0,1]
        j = 4
        o = 0
        self.assertEqual(s.numberOfAlternatingGroups(i,j), o)

    def test_four(self):
        s = Solution()
        i = [0,1,0,1]
        j = 3
        o = 4
        self.assertEqual(s.numberOfAlternatingGroups(i,j), o)

    def test_five(self):
        s = Solution()
        i = [0,1,1]
        j = 3
        o = 1
        self.assertEqual(s.numberOfAlternatingGroups(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)