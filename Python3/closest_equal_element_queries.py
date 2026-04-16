# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import bisect
from collections import defaultdict
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a circular array nums and an array queries.

    For each query i, find the following:
    * The minimum distance between the element at index queries[i] and any other
      index j in the circular array, where nums[j] == nums[queries[i]]. If no
      such index exists, the answer for that query should be -1.

    Return an array answer of the same size as queries, where answer[i]
    represents the result for query i.
    '''
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        indices = defaultdict(list)
        for i in range(2*n):
            j = nums[i%n]
            indices[j].append(i)
        answer = []
        for q in queries:
            a = n
            j = nums[q]
            i = bisect.bisect(indices[j],q)
            a = min(a, indices[j][i] - q)
            i = bisect.bisect_left(indices[j],q+n) - 1
            # if indices[j][i] < q+n:
            a = min(a, q+n - indices[j][i])
            # i = bisect.bisect(indices[j], q)
            # if i < len(indices[j]) - 1:
            #     a = min(a, indices[j][i+1] - indices[j][i])
            # if i > 0:
            #     a = min(a, indices[j][i] - indices[j][i-1])
            answer.append(a if a < n else -1)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,3,1,4,1,3,2]
        j = [0,3,5]
        o = [2,-1,3]
        self.assertEqual(s.solveQueries(i,j), o)

    def test_two(self):
        s = Solution()
        i = [1,2,3,4]
        j = [0,1,2,3]
        o = [-1,-1,-1,-1]
        self.assertEqual(s.solveQueries(i,j), o)

    def test_three(self):
        s = Solution()
        i = [15,1,10,1,20,4,6,14,4,9,4,18]
        j = [0,2,10,6,11,8]
        o = [-1,-1,2,-1,-1,2]
        self.assertEqual(s.solveQueries(i,j), o)

    def test_four(self):
        s = Solution()
        i = [6,12,17,9,16,7,6]
        j = [5,6,0,4]
        o = [-1,1,1,-1]
        self.assertEqual(s.solveQueries(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)