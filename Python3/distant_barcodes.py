# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import Counter
import heapq
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    In a warehouse, there is a row of barcodes, where the ith barcode is
    barcodes[i].

    Rearrange the barcodes so that no two adjacent barcodes are equal. Multiple
    answers may exist, but a solution is guaranteed for each problem.
    '''
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        c = [(-j,i) for i,j in Counter(barcodes).items()]
        heapq.heapify(c)
        answer = []
        while len(c) > 1:
            a,b = heapq.heappop(c)
            x,y = heapq.heappop(c)
            answer.append(b)
            answer.append(y)
            if a + 1 < 0:
                heapq.heappush(c,(a+1,b))
            if x + 1 < 0:
                heapq.heappush(c,(x+1,y))
        if c:
            answer.append(c[0][1])
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,1,1,2,2,2]
        o = [1,2,1,2,1,2]
        self.assertEqual(s.rearrangeBarcodes(i), o)

    def test_two(self):
        s = Solution()
        i = [1,1,1,1,2,2,3,3]
        o = [1,2,1,3,1,2,1,3]
        self.assertEqual(s.rearrangeBarcodes(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)