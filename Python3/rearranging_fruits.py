# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import Counter
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    There are two fruit baskets containing n fruits each. Given two 0-indexed
    integer arrays basket1 and basket2 representing the cost of fruit in each
    basket. The goal is to make both baskets equal. To this the following
    operations may be performed as many times as needed:
    * Choose two indices i and j, and swap the ith fruit of the basket1 with the
      jth fruit of basket2.
    * The cost of the swap is min(basket1[i], basket2[j])

    Two baskets are considered equal if sorting them according to the fruit cost
    makes them exactly the same baskets.

    Return the minimum cost to make both the baskets equal or -1 if impossible.
    '''
    def minCost_incomplete(self, basket1: List[int], basket2: List[int]) -> int:
        # basket1.sort()
        # basket2.sort()
        basket1 = Counter(basket1)
        basket2 = Counter(basket2)
        # get ordered set of all fruit costs
        keys = sorted(set(basket1).union(basket2))
        # check if it is possible to split into two baskets
        for i in keys:
            if (basket1[i] + basket2[i]) % 2:
                return -1
        # review hints
        return

    def minCost_fails(self, basket1: List[int], basket2: List[int]) -> int:
        basket1 = Counter(basket1)
        basket2 = Counter(basket2)
        left = []
        right = []
        for i in set(basket1).union(basket2):
            if (basket1[i] + basket2[i]) % 2:
                return -1
            if basket1[i] < basket2[i]:
                for j in range((basket2[i] - basket1[i]) // 2):
                    right.append(i)
            elif basket1[i] > basket2[i]:
                for j in range((basket1[i] - basket2[i]) // 2):
                    left.append(i)
        left.sort()
        right.sort()
        answer = 0
        i,j = 0, 0
        x,y = len(left) - 1, len(right) - 1
        while i <= x and j <= y:
            if left[i] < right[j]:
                answer += left[i]
                i += 1
                y -= 1
            else:
                answer += right[j]
                j += 1
                x -= 1
        return answer

    def minCost_fail_closer(self, basket1: List[int], basket2: List[int]) -> int:
        basket1.sort()
        basket2.sort()
        c1 = Counter(basket1)
        c2 = Counter(basket2)
        left,right = [], []
        for i in sorted(set(c1).union(c2)):
            if (c1[i] + c2[i]) % 2:
                return -1
            if c1[i] < c2[i]:
                left.extend([i] * ((c2[i] - c1[i]) // 2))
            elif c1[i] > c2[i]:
                right.extend([i] * ((c1[i] - c2[i]) // 2))
        answer = 0
        if basket1[0] == basket2[0]:
            # answer += basket1[0] * (len(left) // 2)
            # if len(left) % 2:
            #     answer += min(left[0], right[0])
            answer += basket1[0] * (len(left) + len(right))
        else:
            answer += min(basket1[0], basket2[0])
            # if len(left) % 2:
            #     answer *= len(left)
            # else:
            #     answer *= len(left) - 1
            #     answer += min(left[1],right[1])
            answer *= len(left) + len(right) - 1
        return answer

    # based on Leetcode editorial
    # https://leetcode.com/problems/rearranging-fruits/editorial/?envType=daily-question&envId=2025-08-02
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        # frequency counter for fruit basket
        # positive values indicate extra fruit in basket1
        # negative values indicate extra fruit in basket2
        freq = Counter()
        # the smallest costing fruit in either basket
        m = float('inf')
        for i,j in zip(basket1, basket2):
            freq[i] += 1
            freq[j] -= 1
            m = min(m, i, j)
        # fruit that need to be moved
        merge = []
        # for key, count in frequency map
        for k, c in freq.items():
            # uneven amount of fruit makes problem impossible
            if c % 2:
                return -1
            merge.extend([k] * (abs(c) // 2))
        # no fruits need move (baskets are equal)
        if not merge:
            return 0
        # want to process low cost fruit first
        merge.sort()
        answer = 0
        # process first half of the array
        for i in merge[:len(merge) // 2]:
            # 2*m is cost of indirect move
            #   ie use smallest fruits in each basket to move small and large merge fruit
            # i is direct cost of small and large fruit
            answer += min(2*m, i)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [4,2,2,2]
        j = [1,4,1,2]
        o = 1
        self.assertEqual(s.minCost(i,j), o)

    def test_two(self):
        s = Solution()
        i = [2,3,4,1]
        j = [3,2,5,1]
        o = -1
        self.assertEqual(s.minCost(i,j), o)

    def test_three(self):
        s = Solution()
        # [8, 14, 43, 43, 80, 80, 84, 88, 88, 100]
        # [43, 80, 88]
        # [8, 14, 32, 32, 42, 42, 68, 68, 84, 100]
        # [32, 42, 68]
        i = [84,80,43,8,80,88,43,14,100,88]
        j = [32,32,42,68,68,100,42,84,14,8]
        # [8, 14, 43, 43, 80, 80, 84, 88, 88, 100]
        # [8, 14, 32, 32, 42, 42, 68, 68, 84, 100]
        # 8 -> 88
        # 8 -> 68
        # [8, 14, 43, 43, 68, 80, 80, 84, 88, 100]
        # [8, 14, 32, 32, 42, 42, 68, 84, 88, 100]
        # 8 -> 80
        # 8 -> 42
        # [8, 14, 42, 43, 43, 68, 80, 84, 88, 100]
        # [8, 14, 32, 32, 42, 68, 80, 84, 88, 100]
        # 8 -> 43
        # 8 -> 32
        # [8, 14, 32, 42, 43, 68, 80, 84, 88, 100]
        # [8, 14, 32, 42, 43, 68, 80, 84, 88, 100]
        o = 48
        self.assertEqual(s.minCost(i,j), o)

    def test_four(self):
        s = Solution()
        i = [1,1,4,8,10,10]
        # [1, 10]
        j = [4,8,12,12,16,16]
        # [12,16]
        # [1,1, 4, 8,10,10]
        # [4,8,12,12,16,16]
        # 1 -> 16
        # [1,4,8,10,10,16]
        # [1,4,8,12,12,16]
        # 1 -> 10
        # 1 -> 12
        # [1,4,8,10,12,16]
        # [1,4,8,10,12,16]
        o = 3
        self.assertEqual(s.minCost(i,j), o)

    def test_six(self):
        s = Solution()
        i = [3,4,4,4,4]
        # [4,4]
        j = [3,5,5,5,5]
        # [5,5]
        # [3,4,4,4,4]
        # [3,5,5,5,5]
        # 4 -> 5
        # 4 -> 5
        # [3,4,4,5,5]
        o = 8
        self.assertEqual(s.minCost(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)