# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import heapq
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        answer = dict()
        flowers.sort()
        f = 0
        heap = []
        for p in sorted(set(people)):
            pass
            while heap and heap[0] < p:
                heapq.heappop(heap)
            if p not in answer:
                while f < len(flowers) and flowers[f][0] <= p:
                    if flowers[f][1] >= p:
                        heapq.heappush(heap, flowers[f][1])
                    f += 1
                answer[p] = len(heap)
        return [answer[p] for p in people]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,10],[3,3]]
        j = [3,3,2]
        o = [2,2,1]
        self.assertEqual(s.fullBloomFlowers(i,j), o)

    def test_two(self):
        s = Solution()
        i = [[1,6],[3,7],[9,12],[4,13]]
        j = [2,3,7,11]
        o = [1,2,2,2]
        self.assertEqual(s.fullBloomFlowers(i,j), o)

    def test_three(self):
        s = Solution()
        i = [[11,11],[24,46],[3,25],[44,46]]
        j = [1,8,26,7,43,26,1]
        o = [0,1,1,1,1,1,0]
        self.assertEqual(s.fullBloomFlowers(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)