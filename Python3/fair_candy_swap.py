# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Alice and Bob have a different total number of candies. Given two integer
    arrays aliceSizes and bobSizes where aliceSizes[i] iis the number of candies
    of the ith box of candy that Alice has and bobSizes[j] is the number of
    candies of the jth box of candy that Bob has.

    Since they are friends, they would like to exchange one candy box each so
    that after the exchange, they both have the same total amount of candy. The
    total amount of candy a person has is the sum of the number of candies in
    each box they have.

    Return an integer array answer where answer[0] is the number of candies in
    the box that Alice must exchange, and answer[1] is the number of candies in
    the box that Bob must exchange. If there are multiple answers, return any
    one of them. It is guaranteed that at least one answer exists.
    '''
    def fairCandySwap_wrong(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        aliceSizes.sort()
        bobSizes.sort()
        aSum = sum(aliceSizes)
        bSum = sum(bobSizes)
        diff = abs(aSum - bSum)
        for b in bobSizes:
            t = abs(2 * diff - b)
            n,m = divmod(t, 2)
            if m == 0 and n in aliceSizes:
                return [t,b]

    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        aSum = sum(aliceSizes)
        bSum = sum(bobSizes)
        aliceSizes = set(aliceSizes)
        diff = abs(aSum - bSum) // 2
        for b in bobSizes:
            t = b - diff
            if t in aliceSizes and bSum - b + t == aSum - t + b:
                return [t, b]
            t = b + diff
            if t in aliceSizes and bSum - b + t == aSum - t + b:
                return [t, b]
        return

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,1]
        j = [2,2]
        o = [1,2]
        self.assertEqual(s.fairCandySwap(i,j), o)

    def test_two(self):
        s = Solution()
        i = [1,2]
        j = [2,3]
        o = [1,2]
        self.assertEqual(s.fairCandySwap(i,j), o)

    def test_three(self):
        s = Solution()
        i = [2]
        j = [1,3]
        o = [2,3]
        self.assertEqual(s.fairCandySwap(i,j), o)

    def test_four(self):
        s = Solution()
        i = [1,2,5]
        j = [2,4]
        o = [5,4]
        self.assertEqual(s.fairCandySwap(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)