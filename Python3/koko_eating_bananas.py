# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Koko loves to eat bananas. There are n piles of bananas, the ith
    pile has piles[i] bananas. The guards have gone and will come back
    in h hours.

    Koko can decide her bananas-per-hour eating speed of k. Each hour,
    she chooses some pile of bananas and eats k bananas from that pile.
    If the pile has less than k bananas, she eats all of them instead
    and will not eat any more bananas during this hour.

    Koko likes to eat slowly but still wants to finish eating all the
    bananas before the guards return.

    Return the minimum integer k such that she can eat all the bananas
    within h hours.
    '''
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # have h time units to eat n piles of piles[i] bananas
        # can eat k bananas per hour
        piles.sort(reverse=True)
        # have to eat a pile every hour due to time restrictions
        if h == len(piles):
            return piles[0]
        # function to check if possible for given k
        def possible(piles:list[int], h:int, k:int) -> bool:
            for i in range(len(piles)):
                if piles[i] <= k:
                    h -= len(piles) - i
                    break
                else:
                    h -= piles[i] // k
                    if piles[i] % k:
                        h -= 1
            return h >= 0
        m = piles[0]
        n = 1
        while m != n:
            k = (m - n) // 2 + n
            if possible(piles, h, k):
                m = k
            else:
                if k == n:
                    break
                n = k
        return m

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [3,6,7,11]
        h = 8
        o = 4
        self.assertEqual(s.minEatingSpeed(i, h), o)

    def test_two(self):
        s = Solution()
        i = [30,11,23,4,20]
        h = 5
        o = 30
        self.assertEqual(s.minEatingSpeed(i, h), o)

    def test_three(self):
        s = Solution()
        i = [30,11,23,4,20]
        h = 6
        o = 23
        self.assertEqual(s.minEatingSpeed(i, h), o)

    def test_four(self):
        s = Solution()
        i = [312884470]
        h = 968709470
        o = 1
        self.assertEqual(s.minEatingSpeed(i, h), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)