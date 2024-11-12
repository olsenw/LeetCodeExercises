# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import bisect
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 2D integer array items where items[i] = [pricei, beautyi] denotes
    the price and beauty of an item respectively.

    Also give a 0-indexed integer array queries. For each queries[j], determine
    the maximum beauty of an item whose price is less than or equal to
    queries[j]. If no such item exists, then the answer to this query is 0.

    Return an array answer of the same length as queries where answer[j] is the
    answer to the jth query.
    '''
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        n = len(items)
        items.sort()
        for i in range(1, n):
            items[i][1] = max(items[i-1][1], items[i][1])
        answer = []
        for q in queries:
            i = bisect.bisect(items, q, key=lambda x: x[0])
            if i == 0:
                answer.append(0)
            else:
                answer.append(items[i-1][1])
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,2],[3,2],[2,4],[5,6],[3,5]]
        j = [1,2,3,4,5,6]
        o = [2,4,5,5,6,6]
        self.assertEqual(s.maximumBeauty(i,j), o)

    def test_two(self):
        s = Solution()
        i = [[1,2],[1,2],[1,3],[1,4]]
        j = [1]
        o = [4]
        self.assertEqual(s.maximumBeauty(i,j), o)

    def test_three(self):
        s = Solution()
        i = [[10,1000]]
        j = [5]
        o = [0]
        self.assertEqual(s.maximumBeauty(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)