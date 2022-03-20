# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    In a row of dominoes, tops[i] and bottoms[i] represent the top and
    bottom halves of the ith domino. (A domino is a tile with two
    numbers from 1 to 6 - one on each half of the tile.)

    It is possible to rotate the ith domino, so that tops[i] and
    bottoms[i] swap values.

    Return the minimum number of rotations so that all the values in
    tops are the same or all the values in bottoms are the same.

    If it cannot be done, return -1.
    '''
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        dominoes = len(tops)
        top = [-1, 0, 0, 0, 0, 0, 0]
        bot = [-1, 0, 0, 0, 0, 0, 0]
        dup = [-1, 0, 0, 0, 0, 0, 0]
        pass
        for t,b in zip(tops,bottoms):
            if t == b:
                dup[t] += 1
            else:
                top[t] += 1
                bot[b] += 1
        pass
        val = max(
            max((j + dup[i], i) for i,j in enumerate(top)),
            max((j + dup[i], i) for i,j in enumerate(bot)),
            # max((j,i) for i,j in enumerate(dup))
        )[1]
        if top[val] + bot[val] + dup[val] >= dominoes:
            return min(top[val], bot[val])
        return -1

    # slick alternate solution saw on accepted solutions detail screen
    # NOT BY ME, UNSURE WHO TO CREDIT
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        # know (if possible) has to be either value of first tile
        for x in (tops[0],bottoms[0]):
            # if value exists in all subsequent tiles
            if all(x in d for d in zip(tops,bottoms)):
                # difference is how many tiles need flipped
                return len(tops)-max(tops.count(x),bottoms.count(x))
        return -1

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [2,1,2,4,2,2]
        j = [5,2,6,2,3,2]
        o = 2
        self.assertEqual(s.minDominoRotations(i,j), o)

    def test_two(self):
        s = Solution()
        i = [3,5,1,2,3]
        j = [3,6,3,3,4]
        o = -1
        self.assertEqual(s.minDominoRotations(i,j), o)

    def test_three(self):
        s = Solution()
        i = [3,3,3,3,3]
        j = [3,3,3,3,3]
        o = 0
        self.assertEqual(s.minDominoRotations(i,j), o)

    def test_four(self):
        s = Solution()
        i = [1,2,1]
        j = [3,3,3]
        o = 0
        self.assertEqual(s.minDominoRotations(i,j), o)

    def test_five(self):
        s = Solution()
        i = [1,1,1]
        j = [1,2,1]
        o = 0
        self.assertEqual(s.minDominoRotations(i,j), o)

    def test_six(self):
        s = Solution()
        i = [1,1,1,4,5]
        j = [2,3,1,1,1]
        o = 2
        self.assertEqual(s.minDominoRotations(i,j), o)

    def test_seven(self):
        s = Solution()
        i = [2,3,2,1,1,1,2,2]
        j = [2,1,2,1,1,3,1,1]
        o = -1
        self.assertEqual(s.minDominoRotations(i,j), o)

    def test_eight(self):
        s = Solution()
        i = [2,1,1,1,2,2,2,1,1,2]
        j = [1,1,2,1,1,1,1,2,1,1]
        o = 2
        self.assertEqual(s.minDominoRotations(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)