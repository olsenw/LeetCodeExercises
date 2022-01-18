# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    There is a long flowerbed in which some of the plots are planted,
    and some are not. However flowers cannot be planeted in adjacent
    plots.

    Given an integer array flowerbed containing 0's and 1's, where 0 
    means empty and 1 means there is already a flower and an integer n,
    return if n new flowers can be planted in the flowerbed without
    violating the no-adjacent-flowers rule.
    '''
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        if len(flowerbed) == 1:
            return flowerbed[0] == 0 and n == 1
        i = 0
        if i+1 < len(flowerbed) and flowerbed[i] == 0 and flowerbed[i+1] == 0:
            n -= 1
        flowerbed[i] = 1
        i += 1
        while i < len(flowerbed)-1 and n >= 0:
            if flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                n -= 1
                flowerbed[i] = 1
            flowerbed[i-1] = 1
            i += 1
        if flowerbed[i] == 0 and flowerbed[i-1] == 0:
            n -= 1
        return n <= 0

    def canPlaceFlowers_alt(self, flowerbed: List[int], n: int) -> int:
        if n == 0 or (len(flowerbed) == 1 and flowerbed[0] == 0):
            return n <= 1
        c = 0
        if flowerbed[0] == 0 and flowerbed[1] == 0:
            flowerbed[0] = 1
            c += 1
        for i in range(1,len(flowerbed)-1):
            if flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1
                c += 1
        if flowerbed[-1] == 0 and flowerbed[-2] == 0:
            flowerbed[-1] = 1
            c += 1
        return n <= c

    # why does operation on parameter n cause it to be slow...
    # if reduce n directly -> very slow, local copy -> very fast.
    def canPlaceFlowers_best(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        c = n
        if (len(flowerbed) == 1 and flowerbed[0] == 0) or (len(flowerbed) > 1 and flowerbed[i] == 0 and flowerbed[i+1] == 0):
            c -= 1
            flowerbed[i] = 1
        i += 1
        while i < len(flowerbed)-1 and c > 0:
            if flowerbed[i] == 0:
                if flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                    c -= 1
                    flowerbed[i] = 1
                    i += 1
            i += 1
        if i == len(flowerbed)-1 and flowerbed[i-1] == 0 and flowerbed[i] == 0:
            c-= 1
        return c <= 0

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,0,0,0,1]
        n = 1
        o = True
        self.assertEqual(s.canPlaceFlowers(list(i), n), o)
        self.assertEqual(s.canPlaceFlowers_alt(
                # why does operation on n cause it to be slow...
                # # if reduce n directly, very slow, local copy very fast.list(i), n), o)
        self.assertEqual(s.canPlaceFlowers_best(list(i), n), o)

    def test_two(self):
        s = Solution()
        i = [1,0,0,0,1]
        n = 2
        o = False
        self.assertEqual(s.canPlaceFlowers(list(i), n), o)
        self.assertEqual(s.canPlaceFlowers_alt(
                # why does operation on n cause it to be slow...
                # # if reduce n directly, very slow, local copy very fast.list(i), n), o)
        self.assertEqual(s.canPlaceFlowers_best(list(i), n), o)

    def test_three(self):
        s = Solution()
        i = [0,0]
        n = 1
        o = True
        self.assertEqual(s.canPlaceFlowers(list(i), n), o)
        self.assertEqual(s.canPlaceFlowers_alt(
                # why does operation on n cause it to be slow...
                # # if reduce n directly, very slow, local copy very fast.list(i), n), o)
        self.assertEqual(s.canPlaceFlowers_best(list(i), n), o)

    def test_four(self):
        s = Solution()
        i = [0,1,0]
        n = 1
        o = False
        self.assertEqual(s.canPlaceFlowers(list(i), n), o)
        self.assertEqual(s.canPlaceFlowers_alt(
                # why does operation on n cause it to be slow...
                # # if reduce n directly, very slow, local copy very fast.list(i), n), o)
        self.assertEqual(s.canPlaceFlowers_best(list(i), n), o)

    def test_five(self):
        s = Solution()
        i = [0,1,0]
        n = 0
        o = True
        self.assertEqual(s.canPlaceFlowers(list(i), n), o)
        self.assertEqual(s.canPlaceFlowers_alt(
                # why does operation on n cause it to be slow...
                # # if reduce n directly, very slow, local copy very fast.list(i), n), o)
        self.assertEqual(s.canPlaceFlowers_best(list(i), n), o)

    def test_six(self):
        s = Solution()
        i = [1,0,0,0,0,1]
        n = 2
        o = False
        self.assertEqual(s.canPlaceFlowers(list(i), n), o)
        self.assertEqual(s.canPlaceFlowers_alt(
                # why does operation on n cause it to be slow...
                # # if reduce n directly, very slow, local copy very fast.list(i), n), o)
        self.assertEqual(s.canPlaceFlowers_best(list(i), n), o)

    def test_seven(self):
        s = Solution()
        i = [1,0,1,0,1,0,1]
        n = 1
        o = False
        self.assertEqual(s.canPlaceFlowers(list(i), n), o)
        self.assertEqual(s.canPlaceFlowers_alt(
                # why does operation on n cause it to be slow...
                # # if reduce n directly, very slow, local copy very fast.list(i), n), o)
        self.assertEqual(s.canPlaceFlowers_best(list(i), n), o)

    def test_eight(self):
        s = Solution()
        i = [1]
        n = 1
        o = False
        self.assertEqual(s.canPlaceFlowers(list(i), n), o)
        self.assertEqual(s.canPlaceFlowers_alt(
                # why does operation on n cause it to be slow...
                # # if reduce n directly, very slow, local copy very fast.list(i), n), o)
        self.assertEqual(s.canPlaceFlowers_best(list(i), n), o)

    def test_nine(self):
        s = Solution()
        i = [1,0,0,0,0,0,1]
        n = 2
        o = True
        self.assertEqual(s.canPlaceFlowers(list(i), n), o)
        self.assertEqual(s.canPlaceFlowers_alt(
                # why does operation on n cause it to be slow...
                # # if reduce n directly, very slow, local copy very fast.list(i), n), o)
        self.assertEqual(s.canPlaceFlowers_best(list(i), n), o)

    def test_ten(self):
        s = Solution()
        i = [0,0,1,0]
        n = 2
        o = False
        self.assertEqual(s.canPlaceFlowers(list(i), n), o)
        self.assertEqual(s.canPlaceFlowers_alt(
                # why does operation on n cause it to be slow...
                # # if reduce n directly, very slow, local copy very fast.list(i), n), o)
        self.assertEqual(s.canPlaceFlowers_best(list(i), n), o)

    def test_eleven(self):
        s = Solution()
        i = [0]
        n = 1
        o = True
        self.assertEqual(s.canPlaceFlowers(list(i), n), o)
        self.assertEqual(s.canPlaceFlowers_alt(
                # why does operation on n cause it to be slow...
                # # if reduce n directly, very slow, local copy very fast.list(i), n), o)
        self.assertEqual(s.canPlaceFlowers_best(list(i), n), o)

    def test_twelve(self):
        s = Solution()
        i = [0]
        n = 1
        o = True
        self.assertEqual(s.canPlaceFlowers(list(i), n), o)
        self.assertEqual(s.canPlaceFlowers_alt(
                # why does operation on n cause it to be slow...
                # # if reduce n directly, very slow, local copy very fast.list(i), n), o)
        self.assertEqual(s.canPlaceFlowers_best(list(i), n), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)