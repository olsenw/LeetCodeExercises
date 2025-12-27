# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an array arr of positive integers, consider all binary trees such
    that:
    * Each node has either 0 or 2 children;
    * The values of arr correspond to the values of each leaf in an in-order
      traversal of the tree.
    * The value of each non-leaf node is equal to the product of the largest
      leaf value in its left and right subtree, respectively.
    
    Among all possible binary trees considered, return the smallest possible sum
    of the values of each non-leaf node. It is guaranteed this sum fits into a
    32-bit integer.

    A node is a leaf if and only if it has zero children.
    '''
    def mctFromLeafValues_errors(self, arr: List[int]) -> int:
        def dp(i:int, j:int) -> int:
            if j - i == 2:
                return arr[i] * arr[i+1]
            if j - i == 1:
                return arr[i]
            if j == i:
                return 0
            answer = 0
            for k in range(i, j):
                answer = max(answer, max(arr[i:k+1]) * max(arr[k+1:j]) + dp(i,k) + dp(k+1,j))
            return answer
        return dp(0, len(arr))

    def mctFromLeafValues_fails(self, arr: List[int]) -> int:
        def dp(i:int, j:int) -> int:
            if j - i == 1:
                return 0
            if j - i == 2:
                return arr[i] * arr[j-1]
            answer = float('inf')
            for k in range(i+1, j-1):
                answer = min(
                    answer,
                    max(arr[i:k]) * max(arr[k:j]) + dp(i,k) + dp(k,j)
                )
            return answer
        return dp(0, len(arr))

    def mctFromLeafValues_fails(self, arr: List[int]) -> int:
        def dp(i:int, j:int) -> int:
            if j - i == 1:
                return arr[i]
            if j - i == 2:
                return arr[i] * arr[j-1]
            answer = float('inf')
            for k in range(i+1, j-1):
                answer = min(
                    answer,
                    dp(i,k) + dp(k,j)
                )
            return answer
        return dp(0, len(arr))

    def mctFromLeafValues(self, arr: List[int]) -> int:
        @cache
        def dp(i:int, j:int) -> int:
            if j - i < 2:
                return 0
            answer = float('inf')
            for k in range(i+1, j):
                answer = min(
                    answer,
                    max(arr[i:k]) * max(arr[k:j]) + dp(i,k) + dp(k,j)
                )
            return answer
        return dp(0, len(arr))

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [6,2,4]
        o = 32
        self.assertEqual(s.mctFromLeafValues(i), o)

    def test_two(self):
        s = Solution()
        i = [4,11]
        o = 44
        self.assertEqual(s.mctFromLeafValues(i), o)

    def test_three(self):
        s = Solution()
        i = [1,1,13,3,3,4,1,1,3,2,8]
        o = 193
        self.assertEqual(s.mctFromLeafValues(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)