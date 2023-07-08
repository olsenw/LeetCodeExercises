# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import heapq
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    There are k bags. Given a 0-indexed integer array weights where weights[i]
    is the weight of the ith marble.

    Divide the marbles into the k bags according to the following rules:
    * No bag is empty.
    * If the ith marble and jth marble are in a bag then all marbles with an
      index between the ith and jth indices should also be in that same bag.
    * If a bag consists of all the marbles with an index from i to j
      inclusively, then the cost of the bag is weights[i] + weights[j].
    
    The score after distributing the marbles is the sum of the costs of all the
    k bags.

    Return the difference between the maximum and minimum scores among marble
    distributions.
    '''
    # O(n log n) time O(n) space
    # based on leetcode solution
    # this works by noting that the first and last weights are always used, and
    # the resulting answers depends where the splits occur for the subarrays
    # placed in each bag.
    # due to how scoring works to calculate the weight values at each split
    # point add the weights to either side of the split points.
    # picture in editorial does much better job showing this.
    def putMarbles(self, weights: List[int], k: int) -> int:
        pairs = sorted(weights[i] + weights[i+1] for i in range(len(weights) - 1))
        return sum(pairs[len(weights) - 2 - i] - pairs[i] for i in range(k-1))

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,3,5,1]
        j = 2
        o = 4
        self.assertEqual(s.putMarbles(i,j), o)

    def test_two(self):
        s = Solution()
        i = [1, 3]
        j = 2
        o = 0
        self.assertEqual(s.putMarbles(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)