# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List
from itertools import chain
import heapq

class Solution:
    '''
    Given an n x n matrix where each of the rows and columns are sorted
    in ascending order, return the kth smallest element in the matrix.

    Note that it is the kth smalles element in the sorted order, not the
    kth distinct element.

    The solution should have a memory complexity better than O(n^2)
    '''
    # pretty sure this is invalid due to memory complexity
    # have to create complete list with n^2 elements in it
    def kthSmallest_sorted(self, matrix: List[List[int]], k: int) -> int:
        return sorted(chain(*matrix))[k - 1]

    # pretty sure that this is also invalid due to memory complexity
    # need a heap of size k and k can potentially be n^2
    def kthSmallest_heap(self, matrix: List[List[int]], k: int) -> int:
        h = [-matrix[-1][-1]] * k
        for m in chain(*matrix):
            heapq.heappushpop(h, -m)
        return -h[0]

    # binary search 
    # O(n log n) time and O(1) space (note n is all elements in array
    # so n^2 by problem description)
    # based on discussion post by alexey_wish
    # https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/discuss/2366916/Python.-Binary-Search.-Very-Simple
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        left = matrix[0][0]
        right = matrix[-1][-1]
        def check(val):
            c = 0
            for i in range(n):
                for j in range(n):
                    if matrix[i][j] <= val:
                        c += 1
            return c < k
        while left < right:
            # mid = (left + right) // 2
            mid = left + right >> 1
            if check(mid):
                left = mid + 1
            else:
                right = mid
        return left

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,5,9],[10,11,13],[12,13,15]]
        j = 8
        o = 13
        self.assertEqual(s.kthSmallest(i,j), o)

    def test_two(self):
        s = Solution()
        i = [[-5]]
        j = 1
        o = -5
        self.assertEqual(s.kthSmallest(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)