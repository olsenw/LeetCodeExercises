# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import heapq
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given two integer arrays nums1 and nums2 sorted in ascending order and an
    integer k.

    Define a pair (u, v) which consists of one element from the first array and
    one element from the second array.
    
    Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.
    '''
    # Memory limit Exceeded (25/35 test cases)
    def kSmallestPairs_memory(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        h = []
        for i in nums1:
            for j in nums2:
                heapq.heappush(h, (i+j, [i, j]))
        answer = []
        for _ in range(k):
            if not h:
                break
            answer.append(heapq.heappop(h)[1])
        return answer

    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        answer = []
        h = []
        for i in range(len(nums1)):
            heapq.heappush(h, (nums1[i] + nums2[0], (i, 0)))
        for _ in range(k):
            if not h:
                break
            i,j = h[0][1]
            answer.append([nums1[i], nums2[j]])
            if j < len(nums2) - 1:
                heapq.heapreplace(h, (nums1[i] + nums2[j + 1], (i, j + 1)))
            else:
                heapq.heappop(h)
        return answer

    '''
    Other people have better solutions that only consider the next two options
    at each step when adding to the heap.
    '''

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,7,11]
        j = [2,4,6]
        k = 3
        o = [[1,2],[1,4],[1,6]]
        self.assertEqual(s.kSmallestPairs(i,j,k), o)

    def test_two(self):
        s = Solution()
        i = [1,1,2]
        j = [1,2,3]
        k = 2
        o = [[1,1],[1,1]]
        self.assertEqual(s.kSmallestPairs(i,j,k), o)

    def test_three(self):
        s = Solution()
        i = [1,2]
        j = [3]
        k = 3
        o = [[1,3],[2,3]]
        self.assertEqual(s.kSmallestPairs(i,j,k), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)