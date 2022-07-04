# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    There are n children standing in a line. Each child is assigned a
    rating value given in the integer array ratings.

    Give candy to these children subject to the following requirements:
    * Each child must have at least one candy.
    * Children with a higher rating get more candies than their
      neighbors.

    Return the minimum number of candies that are needed to distribute
    to the children
    '''
    # Brute force (passes 44/48 test cases)
    # O(n^2) time (n children and a max of n candies per child)
    # O(n) space
    def candy_brute_timeout(self, ratings: List[int]) -> int:
        if len(ratings) == 1:
            return 1
        candy = [1] * len(ratings)
        again = True
        while again:
            again = False
            if (ratings[1] < ratings[0] and candy[1] >= candy[0]):
                candy[0] += 1
                again = True
            for i in range(1, len(ratings) - 1):
                if (ratings[i - 1] < ratings[i] and candy[i-1] >= candy[i]) \
                   or (ratings[i + 1] < ratings[i] and candy[i+1] >= candy[i]):
                    candy[i] += 1
                    again = True
            if (ratings[-2] < ratings[-1] and candy[-2] >= candy[-1]):
                candy[-1] += 1
                again = True
        return sum(candy)

    # Two arrays
    # O(n) time
    # O(n) space
    def candy_two_arrays(self, ratings: List[int]) -> int:
        fore = [1] * len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i - 1] < ratings[i]:
                fore[i] = fore[i-1] + 1
        back = [1] * len(ratings)
        for i in range(len(ratings)-2, -1, -1):
            if ratings[i + 1] < ratings[i]:
                back[i] = back[i+1] + 1
        return sum(max(i,j) for i,j in zip(fore,back))

    '''
    Proud of myself for getting these!

    See Leetcode solutions for way to it O(n) time and O(1) space using
    peaks and valleys analysis.
    '''

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,0,2]
        o = 5
        self.assertEqual(s.candy(i), o)

    def test_two(self):
        s = Solution()
        i = [1,2,2]
        o = 4
        self.assertEqual(s.candy(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)