# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import Counter, List, Dict, Set, Optional

class Solution:
    '''
    Given two 2D integer arrays, items1 and items2, representing two sets of
    items. Each array items has the following properties:
    * items[i] = [valuei, wighti] where valuei represents the value and weighti
      represents the weight of the ith item.
    * The value of each item in items is unique.

    Return a 2D integer array ret where ret[i] = [valuei, weighti], with weighti
    being the sum of weights of all items with value valuei.

    Note: ret should be returned in ascending order by value.
    '''
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        c = Counter()
        for v,w in items1:
            c[v] += w
        for v,w in items2:
            c[v] += w
        return [[i,c[i]] for i in sorted(c.keys())]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,1],[4,5],[3,8]]
        j = [[3,1],[1,5]]
        o = [[1,6],[3,9],[4,5]]
        self.assertEqual(s.mergeSimilarItems(i,j), o)

    def test_two(self):
        s = Solution()
        i = [[1,1],[3,2],[2,3]]
        j = [[2,1],[3,2],[1,3]]
        o = [[1,4],[2,4],[3,4]]
        self.assertEqual(s.mergeSimilarItems(i,j), o)

    def test_three(self):
        s = Solution()
        i = [[1,3],[2,2]]
        j = [[7,1],[2,2],[1,4]]
        o = [[1,7],[2,4],[7,1]]
        self.assertEqual(s.mergeSimilarItems(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)