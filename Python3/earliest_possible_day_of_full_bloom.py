# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    There are n flower seeds. Every seed must be planted first before it can
    begin to grow, then bloom. Planting a seed takes time and so does the growth
    of a seed. Given two 0-indexed integer arrays plantTime and growTime, of
    length n each:
    * plantTime[i] is the number of full days it takes to plant the ith seed.
      Every day, it is possible to plant one seed. Seeds do not have to be
      planted on consecutive days, but planting of a seed is not complete until
      plantTime[i] days have been spent planting the seed.
    * growTime[i] is the number of full days it takes the ith seed to grow after
      being completely planted. After the last day of its growth, the flower
      blooms and stays bloomed forever.
    
    From the beginning of day 0, the seeds can be planted in any order.

    Return the earliest possible day where all seeds are blooming.
    '''

    ''' Greedy
    Sort by descending grow time for planting order
    For each planting check what the bloom day is
        if latter date update latter date to current planting
    '''

    # based on leetcode hints
    # can mix up days (see test 5) order matters for planting because it may
    # bloom later than a following planting
    def earliestFullBloom_wrong(self, plantTime: List[int], growTime: List[int]) -> int:
        # sortedTimes = sorted([(p,g) for p,g in zip(plantTime, growTime)], key=lambda x: (-x[1], x[0]))
        # return sum(p for p,_ in sortedTimes) + sortedTimes[-1][1]
        return sum(plantTime) + min(growTime)

    # based on leetcode solution
    # sorted in descending order of grow time, but needs to do this way to
    # ensure counting order remains correct
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        planting, latest = 0, 0
        for i in sorted(range(len(plantTime)), key=lambda x: -growTime[x]):
            planting += plantTime[i]
            latest = max(latest, planting + growTime[i])
        return latest

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,4,3]
        j = [2,3,1]
        o = 9
        self.assertEqual(s.earliestFullBloom(i,j), o)

    def test_two(self):
        s = Solution()
        i = [1,2,3,2]
        j = [2,1,2,1]
        o = 9
        self.assertEqual(s.earliestFullBloom(i,j), o)

    def test_three(self):
        s = Solution()
        i = [1]
        j = [1]
        o = 2
        self.assertEqual(s.earliestFullBloom(i,j), o)

    def test_four(self):
        s = Solution()
        i = [27,5,24,17,27,4,23,16,6,26,13,17,21,3,9,10,28,26,4,10,28,2]
        j = [26,9,14,17,6,14,23,24,11,6,27,14,13,1,15,5,12,15,23,27,28,12]
        o = 348
        self.assertEqual(s.earliestFullBloom(i,j), o)

    def test_five(self):
        s = Solution()
        i = [1,2]
        j = [100,3]
        o = 101
        self.assertEqual(s.earliestFullBloom(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)