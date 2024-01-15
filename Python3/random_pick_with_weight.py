# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from bisect import bisect
from collections import deque
from itertools import accumulate
from random import randint, shuffle,random
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution_Memory_Limit_Exceeded:
    '''
    Given a 0-indexed array of positive integers w where w[i] describes the
    weight of the ith index.

    Implement the function pickIndex, such that it randomly picks an index in
    the range [0, w.length - 1] (inclusive) and returns it. The probability of
    picking an index i is w[i] / sum(w)
    '''
    # way too much memory O(max(w) * w.length) [ie 10^5 * 10^4] 
    def __init__(self, w: List[int]):
        self.n = len(w)
        self.s = sum(w)
        l = []
        for i,j in enumerate(w):
            l.extend([i]*j)
        shuffle(l)
        self.q = deque(l)

    def pickIndex(self) -> int:
        self.q.append(self.q[0])
        return self.q.popleft()

# based on solution by drblessing
# https://leetcode.com/problems/random-pick-with-weight/solutions/671921/python-3-simple-solution/
class Solution:

    def __init__(self, w: List[int]):
        # create normalized range of weighted values for each index
        # [1,3,3,1] -> [1/8,3/8,3/8,1/8] -> [1/8,4/8,7/8,1]
        self.w = list(accumulate(w))
        # self.w = [i / self.w[-1] for i in self.w]
        
        # self.s = sum(w)
        # self.w = [i / self.s for i in accumulate(w)]
        
        # self.w = list(accumulate([i / self.s for i in w]))

    def pickIndex(self) -> int:
        return bisect.bisect_left(self.w, random.randint(1,self.w[-1]))

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution([1])
        self.assertEqual(s.pickIndex(), 0)

    def test_two(self):
        s = Solution([1,3])
        answers = [0,0]
        for _ in range(1000):
            answers[s.pickIndex()] += 1
        self.assertAlmostEqual(answers[0] / 1000, 0.25)
        self.assertAlmostEqual(answers[1] / 1000, 0.75)

if __name__ == '__main__':
    unittest.main(verbosity=2)