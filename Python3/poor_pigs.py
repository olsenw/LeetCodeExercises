# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    There are buckets buckets of liquid, where exactly one of the
    buckets is poisonous. To figure out which one is poisonous, feed
    some number of pigs the liquid to see whether they will die or not.
    Unfortunately, there are only minutesToTest minutes to determine
    which bucket is poisonous.

    Pigs can be feed according to these steps:
    1) Choose some live pigs to feed.
    2) For each pig, choose which buckets to feed it. The pig will
       consume all the chosen buckets simultaneously and will take no
       time.
    3) Wait for minutesToDie minutes. No other pigs may be fed during
       this time.
    4) After minutesToDie minutes have passed any pigs that have been
       fed the poisonous bucket will die, and all others will survive.
    5) Repeat the process until time has run out.

    Given buckets, minutesToDie, and minutesToTest, return the minimum
    number of pigs needed to figure out which bucket is poisonous within
    the allotted time.
    '''
    # leetcode hint helped once figured it out
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        tests = minutesToTest // minutesToDie
        pigs = 0
        while (tests + 1) ** pigs < buckets:
            pigs += 1
        return pigs

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 1000
        j = 15
        k = 60
        o = 5
        self.assertEqual(s.poorPigs(i,j,k), o)

    def test_two(self):
        s = Solution()
        i = 4
        j = 15
        k = 15
        o = 2
        self.assertEqual(s.poorPigs(i,j,k), o)

    def test_three(self):
        s = Solution()
        i = 4
        j = 15
        k = 30
        o = 2
        self.assertEqual(s.poorPigs(i,j,k), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)