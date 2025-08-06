# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import bisect
from collections import Counter
import math
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given two arrays of integers, fruits and baskets, each of length n, where
    fruits[i] represents the quantity of the ith type of fruit, baskets[j]
    represents the capacity of the jth basket.

    From left to right, place the fruits according to these rules:
    * Each fruit type must be placed in the leftmost available basket with a
      capacity greater than or equal to the quantity of that fruit.
    * Each basket can hold only one type of fruit.
    * If a fruit cannot be placed in any basket, it remains unplaced.

    Return the number of fruit types that remain unplaced after all possible
    allocations are made.
    '''
    def numOfUnplacedFruits_bail(self, fruits: List[int], baskets: List[int]) -> int:
        answer = 0
        # does not work because order of baskets matters more than size
        order:Dict[int, List] = dict()
        for i,j in enumerate(baskets):
            if j not in order:
                order[j] = [i]
            else:
                order[j].append(i)
        keys = sorted(order)
        # does not work because order matters
        order = Counter(baskets)
        for f in fruits:
            i = bisect.bisect(order, f)
        return answer

    # brute forced O(n^2)
    def numOfUnplacedFruits_brute(self, fruits: List[int], baskets: List[int]) -> int:
        answer = len(fruits)
        for f in fruits:
            for i,j in enumerate(baskets):
                if j >= f:
                    baskets[i] *= -1
                    answer -= 1
                    break
        return answer

    # same problem does not maintain order (ie place if bigger basket if first)
    def numOfUnplacedFruits_failed(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(baskets)
        available = [True] * n
        baskets = sorted([j,i] for i,j in enumerate(baskets))
        answer = 0
        for f in fruits:
            i = bisect.bisect(baskets, [f,0])
            for i in range(i,n):
                if available[i]:
                    available[i] = False
                    break
            if i == n:
                answer += 1
            pass
        return answer

    # based on LeetCode Square Root Decomposition editorial
    # https://leetcode.com/problems/fruits-into-baskets-iii/editorial/?envType=daily-question&envId=2025-08-06
    # divide basket into sqrt(n) sections and then update individual section manually when fill with fruit
    # O(n * sqrt(n)) = O(n ^ 1.5)
    # barely under the complexity requirements
    def numOfUnplacedFruits_square_root_decomposition(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(baskets)
        m = math.isqrt(n)
        answer = n
        # find maximum basket in a gie section
        sections = (n + m - 1) // m
        maxB = [0] * sections
        for i in range(n):
            # can calculate which section a given index is in
            maxB[i // m] = max(maxB[i // m], baskets[i])
        # iterate over all fruits
        for f in fruits:
            # iterate over all sections
            for i in range(sections):
                if maxB[i] < f:
                    # no baskets in this section
                    continue
                chosen = False
                maxB[i] = 0
                # section i has a useful basket
                for j in range(m):
                    # true index of basket j in section i
                    k = i * m + j
                    # guard condition for running out of baskets
                    if not (k < n):
                        break
                    if baskets[k] >= f and not chosen:
                        # left most basket found (set to zero to represent used)
                        baskets[k] = 0
                        chosen = True
                    maxB[i] = max(baskets[k], maxB[i])
                answer -= 1
                # found useful basket
                break
        return answer

    # based on LeetCode Segment Tree + Binary Search editorial
    # https://leetcode.com/problems/fruits-into-baskets-iii/editorial/?envType=daily-question&envId=2025-08-06
    # use segment tree to track maximum size of basket over a binary subdivisions
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        class SegmentTree:
            def __init__(self, left, right):
                self.left = left
                self.leftSegment = None
                self.right = right
                self.rightSegment = None
                self.value = baskets[left]
                if left < right:
                    m = left + (right - left) // 2
                    pass
                    self.leftSegment = SegmentTree(left, m)
                    self.rightSegment = SegmentTree(m+1, right)
                    self.value = max(self.leftSegment.value, self.rightSegment.value)
            def __repr__(self):
                return f'{self.value} ({self.left},{self.right})'
            def _update(self, fruit) -> None:
                if self.leftSegment is None:
                    self.value = 0
                    return
                if fruit <= self.leftSegment.value:
                    self.leftSegment.update(fruit)
                else:
                    self.rightSegment.update(fruit)
                self.value = max(self.leftSegment.value, self.rightSegment.value)
            def update(self, fruit:int) -> bool:
                if fruit > self.value:
                    return False
                self._update(fruit)
                return True
        n = len(baskets)
        tree = SegmentTree(0,n-1)
        answer = 0
        for fruit in fruits:
            if not tree.update(fruit):
                answer += 1
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [4,2,5]
        j = [3,5,4]
        o = 1
        self.assertEqual(s.numOfUnplacedFruits(i,j), o)

    def test_two(self):
        s = Solution()
        i = [3,6,1]
        j = [6,4,7]
        o = 0
        self.assertEqual(s.numOfUnplacedFruits(i,j), o)

    def test_three(self):
        s = Solution()
        i = [1,1,4]
        j = [4,1,1]
        o = 1
        self.assertEqual(s.numOfUnplacedFruits(i,j), o)

    def test_four(self):
        s = Solution()
        i = [29,29]
        j = [29,9]
        o = 1
        self.assertEqual(s.numOfUnplacedFruits(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)