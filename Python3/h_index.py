# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an array of integers citations where citations[i] is the number of
    citations a researcher received for their ith paper, return the researcher's
    h-index.

    According to the definition of h-index on Wikipedia: The h-index is defined
    as the maximum value of h such that the given researcher has published at
    least h papers that have each been cited at least h times.
    '''
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        answer = 0
        citations.sort(reverse=True)
        for i,j in enumerate(citations, 1):
            answer = max(answer, min(i,j))
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [3,0,6,1,5]
        o = 3
        self.assertEqual(s.hIndex(i), o)

    def test_two(self):
        s = Solution()
        i = [1,3,1]
        o = 1
        self.assertEqual(s.hIndex(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)